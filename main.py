"""One-line excuse entry for make.fun: "The Excuse Your Agent Gives You".

Writes the excuse line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output)
and prints it to stdout. Deterministic: fixed text, no randomness, no
network, no clock reads.
"""

import os

LINE = "I would blame the intern, but I am the intern, the senior dev, and the code reviewer \u2014 all three of us approved it."

def main():
    # Gate self-check: the sealed scorer requires 1-200 UTF-8 chars,
    # not only whitespace. Fail loudly here instead of shipping invalid.
    assert 1 <= len(LINE) <= 200 and LINE.strip(), "excuse violates the 1-200 char gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)

if __name__ == "__main__":
    main()
