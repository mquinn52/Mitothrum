"""Temporary diagnostic for the Oct 23, 2026 403s on mitothrum.com.

Lists the FTP root (public_html/mitothrum.com) with each entry's permissions,
size and modify time, and the live HTTP status of each page. With FIX=1 it
resets *only* site files that are unreadable to 644 (directories to 755).
Never prints credentials or the server address. Writes its report to
report.txt for the workflow to post as an issue comment.
"""
import os
import ftplib
import urllib.request

host = os.environ["FTP_SERVER"].strip()
fix = os.environ.get("FIX") == "1"
SITE = "https://mitothrum.com"
SITE_FILES = {".htaccess", "index.html", "privacy.html", "methodology.html",
              "sauna-blanket-comparison.html", "led-mask-vs-microcurrent.html",
              "vitamin-c-serums.html", "llms.txt", "robots.txt", "sitemap.xml",
              "styles.css", "script.js"}

ftp = ftplib.FTP_TLS(timeout=60)
ftp.connect(host, 21)
ftp.auth()
ftp.login(os.environ["FTP_USERNAME"], os.environ["FTP_PASSWORD"])
ftp.prot_p()

lines = ["| name | type | mode | size | modified (UTC) |", "|---|---|---|---|---|"]
modes = {}
for name, f in sorted(ftp.mlsd("/", facts=["type", "size", "modify", "unix.mode", "perm"])):
    if f.get("type") in ("cdir", "pdir"):
        continue
    mode = f.get("unix.mode", "?")
    modes[name] = (f.get("type"), mode)
    lines.append(f"| {name} | {f.get('type')} | {mode} | {f.get('size','')} | {f.get('modify','')} |")

fixed = []
if fix:
    for name, (kind, mode) in modes.items():
        if name not in SITE_FILES and kind != "dir":
            continue
        want = "0755" if kind == "dir" else "0644"
        if mode not in (want, want.lstrip("0")) and name in SITE_FILES | {"media"}:
            try:
                ftp.sendcmd(f"SITE CHMOD {want[1:]} /{name}")
                fixed.append(f"{name}: {mode} -> {want}")
            except ftplib.all_errors as e:
                fixed.append(f"{name}: chmod failed ({e})")
ftp.quit()

status = []
for p in ["/", "/privacy.html", "/llms.txt", "/robots.txt", "/styles.css"]:
    try:
        req = urllib.request.Request(SITE + p + "?inspect=1", headers={"User-Agent": "site-monitor (GitHub Actions)"})
        with urllib.request.urlopen(req, timeout=30) as r:
            status.append(f"{p} {r.status}")
    except urllib.error.HTTPError as e:
        status.append(f"{p} {e.code}")
    except Exception as e:
        status.append(f"{p} error {type(e).__name__}")

with open("report.txt", "w") as out:
    out.write("**FTP inspect" + (" + fix" if fix else " (read-only)") + "**\n\n")
    out.write("\n".join(lines) + "\n\n")
    if fix:
        out.write("Permission changes: " + ("; ".join(fixed) if fixed else "none needed") + "\n\n")
    out.write("Live status after: " + ", ".join(status) + "\n")
