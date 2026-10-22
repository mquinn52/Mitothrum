"""Refuse to deploy unless the FTP login is rooted at the mitothrum.com site folder.

The deploy uploads into the root of the FTP account, so that account must be
rooted at public_html/mitothrum.com. This check stops a mistake in the account
or in the secrets from putting Mitothrum files anywhere else, above all into the
waterdamagegwinnett.com site (its files live in public_html).

Read-only: it lists names and sizes, never writes or deletes. It prints verdicts
only, never credentials or the server address.
"""
import os
import sys
import ftplib

host = os.environ["FTP_SERVER"].strip()
user = os.environ["FTP_USERNAME"]
password = os.environ["FTP_PASSWORD"]

# Names that exist in the waterdamagegwinnett.com site folder, not in this one.
WDG_MARKERS = {
    "duluth.html",
    "burst-pipe.html",
    "flooded-basement.html",
    "google212c576ac40cf138.html",
    "es",
}

ftp = ftplib.FTP_TLS(timeout=60)
ftp.connect(host, 21)
ftp.auth()
ftp.login(user, password)
ftp.prot_p()
ftp.voidcmd("TYPE I")

names = {}
for name, facts in ftp.mlsd("/", facts=["type"]):
    kind = facts.get("type", "")
    if kind in ("cdir", "pdir"):
        continue
    names[name] = "dir" if kind == "dir" else "file"

wdg_found = sorted(WDG_MARKERS & set(names))
has_media = names.get("media") == "dir"
has_state = ".ftp-deploy-sync-state.json" in names

try:
    htaccess = f"{ftp.size('/.htaccess')} bytes"
except ftplib.all_errors:
    htaccess = "none"

try:
    logo = "present" if ftp.size("/media/logo/mitothrum-mark-amber-1024.png") else "empty"
except ftplib.all_errors:
    logo = "not present"

ftp.quit()

summary = (
    f"FTP root has {len(names)} entries. media/ folder: {'yes' if has_media else 'NO'}. "
    f"WDG site files: {', '.join(wdg_found) if wdg_found else 'none'}. "
    f"Earlier deploy state file: {'yes' if has_state else 'no'}. "
    f"Existing .htaccess: {htaccess}. Logo PNG: {logo}."
)
print(summary)

problems = []
if wdg_found:
    problems.append(
        "this FTP root contains files of the waterdamagegwinnett.com site "
        f"({', '.join(wdg_found)}); refusing to deploy Mitothrum into it"
    )
if not has_media:
    problems.append(
        "no media/ folder at the FTP root; this is not the mitothrum.com site folder"
    )

if problems:
    print("::error title=Wrong FTP target::" + "; ".join(problems))
    print("::notice title=FTP target details::" + summary)
    sys.exit(1)

print("::notice title=FTP target OK::Rooted at the mitothrum.com site folder. " + summary)
