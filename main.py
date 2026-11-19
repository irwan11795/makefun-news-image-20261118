#!/usr/bin/env python3
"""news-image-20261118 entry: writes the pre-rendered front page to /output/entry.png.

The image is a fixed asset in this repo (entry.png), drawn by the author with
gen.py (PIL only, no network, fully deterministic — re-running gen.py produces
byte-identical output). This program copies it byte-for-byte, so every run
writes identical output. No network access, standard library only.
"""
import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT = "/output/entry.png"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(SRC, OUT)
    with open(OUT, "rb") as f:
        digest = hashlib.sha256(f.read()).hexdigest()
    print("wrote", OUT, digest)


if __name__ == "__main__":
    main()
