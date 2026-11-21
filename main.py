#!/usr/bin/env python3
"""news-image-20261120: Friday 20 November 2026 in one image.

The entry image (entry.png, 1024x1024, drawn at build time) is copied to
the grader's output directory. Standard library only, no network, no
other file writes: the program reads one file beside itself and writes
one file to the output directory, so both runs write identical bytes.

Layout (my own front page): masthead "Friday 20 November 2026", a
six-number stat strip, a region bar, a UTC timeline, three hero stories
(Kyiv bridges, Cyclone Akvan, the AI sell-off), ten numbered feature
stories, a 22-story "also" list, a numbered world map, and a red DATE
CHECK box listing the 19 November news deliberately left out.
"""
import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(outdir, exist_ok=True)
    dst = os.path.join(outdir, "entry.png")
    shutil.copyfile(src, dst)
    size = os.path.getsize(dst)
    if size > 1048576:
        print("entry.png exceeds 1 MiB", file=sys.stderr)
        return 1
    print("wrote %s (%d bytes)" % (dst, size))
    return 0


if __name__ == "__main__":
    sys.exit(main())
