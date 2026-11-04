"""Writes the build version into index.html (block // <GEN:VERSION> ... // </GEN:VERSION>).

Run before every commit with the commit message of the upcoming change:
    python tools/make_version.py "Kurze Beschreibung der Änderung"
The version is the number of commits on main plus one; the tooltip in the debug panel (F3)
lists this change and the previous ones from `git log`.
"""
import datetime, json, os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
msg = " ".join(sys.argv[1:]).strip()
git = lambda *a: subprocess.run(["git", "-C", ROOT, *a], capture_output=True, text=True).stdout.strip()
count = int(git("rev-list", "--count", "HEAD") or 0) + 1
log = [l for l in git("log", "-12", "--date=format:%d.%m. %H:%M", "--pretty=%ad|%s").splitlines() if l]
now = datetime.datetime.now().strftime("%d.%m. %H:%M")
changes = ([f"{now}|{msg}"] if msg else []) + log
changes = [{"date": c.split("|", 1)[0], "text": c.split("|", 1)[1]} for c in changes[:12]]
block = ("// <GEN:VERSION> written by tools/make_version.py - do not edit by hand\n"
         f"const BUILD = {json.dumps({'version': count, 'date': datetime.date.today().isoformat(), 'changes': changes}, ensure_ascii=False)};\n"
         "// </GEN:VERSION>")
p = os.path.join(ROOT, "index.html")
s = open(p, encoding="utf-8").read()
b, e = "// <GEN:VERSION>", "// </GEN:VERSION>"
if b in s:
    i, j = s.index(b), s.index(e) + len(e)
    s = s[:i] + block + s[j:]
else:
    anchor = "const ECON = DATA.economy;"
    s = s.replace(anchor, block + "\n" + anchor, 1)
open(p, "w", encoding="utf-8").write(s)
print(f"Version {count}: {msg or '(ohne Nachricht)'}")
