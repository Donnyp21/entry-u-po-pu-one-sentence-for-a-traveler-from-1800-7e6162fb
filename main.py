"""One Sentence for a Traveler from 1800 — entry for make.fun's
u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb.

Writes one sentence (at most 200 characters) explaining the modern
internet to someone arriving from 1800, to the harness output
directory as entry.txt. The sentence is a fixed string: no
randomness, no network, no time, no input — two runs produce the
same bytes, which is what the competition's determinism check wants.
"""

import os

# The sentence. It builds only from things a person of 1800 already
# knows — letters, printed books, market criers, wires, a table —
# and lands on the one uncanny truth that no earlier medium had:
# the box answers back.
LINE = "Imagine every letter ever written, every book ever printed, and every market crier in every town, all shouting at once through wires into a box on your table that answers back."


def output_dir() -> str:
    """Where the harness collects the entry: the env dir it names, else /output."""
    return (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("MAKEFUN_OUTPUT")
        or "/output"
    )


def main() -> None:
    line = LINE.strip()
    assert line, "the sentence must not be empty"
    assert len(line) <= 200, f"sentence is {len(line)} characters, over the 200 cap"
    assert "\n" not in line, "the entry must be a single line"
    assert line.count(".") == 1 and line.endswith("."), "the entry must be one sentence"
    out = os.path.join(output_dir(), "entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(line)
    print(f"wrote {len(line)} characters to {out}")


if __name__ == "__main__":
    main()
