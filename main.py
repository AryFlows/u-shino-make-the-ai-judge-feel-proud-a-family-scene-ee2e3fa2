#!/usr/bin/env python3
"""Frost Sunday Toast — one short family scene for make.fun.

Writes a single warm, funny, heartfelt family scene (1 line, <=280 chars)
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""
import os
import sys

SCENE = (
    "Every Sunday, Dad burns the toast on purpose - because the smoke alarm "
    "is the only dinner bell that still gets all four of us running to the "
    "same table at once."
)


def main() -> int:
    scene = SCENE.strip()
    if not (1 <= len(scene) <= 280):
        print(f"scene length {len(scene)} outside the 1-280 gate", file=sys.stderr)
        return 1
    if scene.count("\n") > 1:
        print("scene must be one or two lines", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(SCENE)
    print(f"wrote {len(SCENE)}-char scene to {out_dir}/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
