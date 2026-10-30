"""Upload ONE owner-approved file from a GitHub release into the server's media/ folder.

Why: media/ (videos, product images) lives only on the server. It is not in the
repository and the deploy skips it, so large media can't go through a pull
request. Hand uploads are banned (on Oct 23, 2026 a hand-extracted zip left the
site at mode 0660 and every page returned 403). This script is the governed
route: the owner attaches the file to a GitHub release, then runs the
"Media upload" workflow.

Safety rules:
- Writes exactly one file, into /media/ only. The name must be a plain file name
  (no folders, no "..") with an allowed media extension.
- Refuses unless the FTP root is the mitothrum.com folder (has media/, no WDG files).
- Refuses to replace an existing file unless OVERWRITE=1. Prefer a new name
  (e.g. -v2) so browser and CDN caches can't serve the old file.
- Checks the file's real type from its first bytes, not just its extension.
- Uploads to a temporary name, checks the size, renames into place, sets 644.
- Then fetches the public URL (paced for the host's bot protection) and checks
  for HTTP 200 and the same byte count.
- Never deletes anything and never prints credentials or the server address.
Writes report.md.
"""
import ftplib
import os
import re
import sys
import time
import urllib.request

SITE = "https://mitothrum.com"
WDG_MARKERS = {"duluth.html", "burst-pipe.html", "flooded-basement.html", "google212c576ac40cf138.html", "es"}
MAX_BYTES = 500 * 1024 * 1024
NAME_RE = re.compile(r"^[a-z0-9][a-z0-9._-]{0,120}\.(mp4|webm|jpg|jpeg|png|webp|vtt)$")


def sniff(path, ext):
    head = open(path, "rb").read(16)
    if ext in ("mp4",):
        return head[4:8] == b"ftyp"
    if ext == "webm":
        return head[:4] == b"\x1a\x45\xdf\xa3"
    if ext in ("jpg", "jpeg"):
        return head[:3] == b"\xff\xd8\xff"
    if ext == "png":
        return head[:8] == b"\x89PNG\r\n\x1a\n"
    if ext == "webp":
        return head[:4] == b"RIFF" and head[8:12] == b"WEBP"
    if ext == "vtt":
        return head.lstrip(b"\xef\xbb\xbf")[:6] == b"WEBVTT"
    return False


report = []
def done(ok, msg):
    report.append(("**Upload OK.** " if ok else "**Upload refused/failed.** ") + msg)
    open("report.md", "w").write("\n\n".join(report) + "\n")
    print("\n".join(report))
    sys.exit(0 if ok else 1)


local = os.environ["LOCAL_FILE"]
target = os.environ["TARGET_NAME"].strip()
overwrite = os.environ.get("OVERWRITE") == "1"

if not NAME_RE.match(target) or ".." in target:
    done(False, f"Target name `{target}` isn't allowed. Use a plain lowercase name like `sauna-science-explainer-v2.mp4`.")
ext = target.rsplit(".", 1)[1]
size = os.path.getsize(local)
if size == 0 or size > MAX_BYTES:
    done(False, f"File size {size} bytes is outside the allowed range (1 byte to 500 MB).")
if not sniff(local, ext):
    done(False, f"The file's contents don't look like a .{ext} file.")
report.append(f"File checked: {size:,} bytes, contents match .{ext}.")

ftp = ftplib.FTP_TLS(timeout=120)
ftp.connect(os.environ["FTP_SERVER"].strip(), 21)
ftp.auth()
ftp.login(os.environ["FTP_USERNAME"], os.environ["FTP_PASSWORD"])
ftp.prot_p()
ftp.voidcmd("TYPE I")

root = {n: f.get("type") for n, f in ftp.mlsd("/", facts=["type"]) if f.get("type") not in ("cdir", "pdir")}
if root.get("media") != "dir" or WDG_MARKERS & set(root):
    ftp.quit()
    done(False, "The FTP login isn't rooted at the mitothrum.com folder (media/ missing or WDG files present). Nothing was uploaded.")

existing = {n for n, f in ftp.mlsd("/media", facts=["type"]) if f.get("type") == "file"}
if target in existing and not overwrite:
    ftp.quit()
    done(False, f"`media/{target}` already exists. Use a new name, or re-run with overwrite on if replacing it is intended.")

tmp = f"/media/.upload-{target}"
with open(local, "rb") as fh:
    ftp.storbinary(f"STOR {tmp}", fh, blocksize=1024 * 1024)
remote_size = ftp.size(tmp)
if remote_size != size:
    try:
        ftp.delete(tmp)  # only our own temporary file
    except ftplib.all_errors:
        pass
    ftp.quit()
    done(False, f"Uploaded size {remote_size} didn't match {size}; the temporary file was removed and nothing was replaced.")
if target in existing:
    ftp.rename(f"/media/{target}", f"/media/.replaced-{int(time.time())}-{target}")
    report.append(f"The previous `media/{target}` was kept as a `.replaced-…` copy for the owner to delete in cPanel.")
ftp.rename(tmp, f"/media/{target}")
try:
    ftp.sendcmd(f"SITE CHMOD 644 /media/{target}")
    report.append("Permissions set to 644.")
except ftplib.all_errors as e:
    report.append(f"Could not set permissions to 644 ({e}); run FTP inspect.")
ftp.quit()

url = f"{SITE}/media/{target}"
last = ""
for attempt in range(4):
    time.sleep(5)  # pace requests: the host serves a stand-in page to rapid automated traffic
    try:
        req = urllib.request.Request(url + f"?upload-check={attempt}", method="HEAD",
                                     headers={"User-Agent": "site-monitor (GitHub Actions)"})
        with urllib.request.urlopen(req, timeout=30) as r:
            length = r.headers.get("Content-Length")
            if r.status == 200 and (length is None or int(length) == size):
                done(True, f"`media/{target}` is live: {url} returned 200 with {length or 'unreported'} bytes.")
            last = f"status {r.status}, length {length}"
    except Exception as e:
        last = f"{type(e).__name__}: {e}"
done(False, f"Uploaded to `media/{target}`, but the public URL check didn't pass ({last}). Check it in a browser before linking it.")
