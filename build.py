"""
build.py — Hasibul Shanto Portfolio Timeline
─────────────────────────────────────────────
Drop images into works/YEAR/ folders, then run:
    python build.py

Supported formats: jpg, jpeg, png, webp, gif
Writes manifest.json → page auto-populates on next load.
"""

import os
import json

WORKS_DIR   = "works"
MANIFEST    = "manifest.json"
YEARS       = ["2021", "2022", "2023", "2024", "2025"]
EXTENSIONS  = {".jpg", ".jpeg", ".png", ".webp", ".gif"}

manifest = {}

for year in YEARS:
    folder = os.path.join(WORKS_DIR, year)
    os.makedirs(folder, exist_ok=True)   # create folder if missing

    files = []
    if os.path.isdir(folder):
        for f in sorted(os.listdir(folder)):
            if os.path.splitext(f)[1].lower() in EXTENSIONS:
                # forward-slash paths work in all browsers
                files.append(f"{WORKS_DIR}/{year}/{f}")

    manifest[year] = files
    status = f"  {len(files)} image(s)" if files else "  (empty)"
    print(f"{year}{status}")

with open(MANIFEST, "w") as fh:
    json.dump(manifest, fh, indent=2)

total = sum(len(v) for v in manifest.values())
print(f"\n✓ manifest.json updated — {total} image(s) total")
print("  Push to GitHub and reload the page.")
