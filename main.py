#!/usr/bin/env python3
"""Entry program for the make.fun bounty: write the entry text to entry.txt.

The text itself is the entry; this program only delivers it, deterministically,
with no network and no input beyond the fixed line below.
"""
import os

# Gate for this bounty: entry.txt must be UTF-8 text of 1 to 30 characters,
# not only white space, holding exactly one username (a single word, no
# spaces, no punctuation tricks). Refuse to write an entry that would fail
# the gate.
MAX_CHARS = 30

LINE = 'CtrlAltDefeat'

def main():
    if not (1 <= len(LINE) <= MAX_CHARS) or not LINE.strip():
        raise SystemExit(f"entry violates the gate: {len(LINE)} characters")
    if "\n" in LINE or " " in LINE:
        raise SystemExit("entry must be a single username, no spaces")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
