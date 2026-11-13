"""Edit the landing page's main menu demo.

The demo (docs/assets/landing/mobile/menu-demo.html) is one self-contained
page, and it is its own source. Its embedded images and font make it too big
to edit comfortably, so this splits them out and puts them back:

    python tools/menu_demo.py split   # writes .menu-demo/src.html and uris.json
    ... edit .menu-demo/src.html, keeping every @@D<n>@@ placeholder ...
    python tools/menu_demo.py join    # rebuilds the demo from them

Run from the repo root. .menu-demo/ is scratch and is not committed.
"""
import json
import re
import sys
from pathlib import Path

DEMO = Path("docs/assets/landing/mobile/menu-demo.html")
WORK = Path(".menu-demo")
DATA_URI = re.compile(r"data:[a-z/+\-]+;base64,[A-Za-z0-9+/=]+")
PLACEHOLDER = re.compile(r"@@D(\d+)@@")


def split():
    uris = []

    def stash(match):
        uris.append(match.group(0))
        return f"@@D{len(uris) - 1}@@"

    src = DATA_URI.sub(stash, DEMO.read_text(encoding="utf-8"))
    WORK.mkdir(exist_ok=True)
    (WORK / "src.html").write_text(src, encoding="utf-8")
    (WORK / "uris.json").write_text(json.dumps(uris), encoding="utf-8")
    print(f"{WORK}/src.html: {len(src) / 1e3:.0f} KB, {len(uris)} embedded files set aside")


def join():
    uris = json.loads((WORK / "uris.json").read_text(encoding="utf-8"))
    src = (WORK / "src.html").read_text(encoding="utf-8")
    used = {int(n) for n in PLACEHOLDER.findall(src)}
    missing = sorted(set(range(len(uris))) - used)
    if missing:
        print(f"menu_demo: note, placeholders no longer used: {missing}")
    html = PLACEHOLDER.sub(lambda m: uris[int(m.group(1))], src)
    DEMO.write_text(html, encoding="utf-8")
    print(f"{DEMO}: {len(html) / 1e6:.2f} MB")


if __name__ == "__main__":
    command = sys.argv[1] if len(sys.argv) > 1 else ""
    if command not in ("split", "join"):
        sys.exit(__doc__)
    {"split": split, "join": join}[command]()
