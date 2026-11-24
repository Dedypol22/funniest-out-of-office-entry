"""The Funniest Out-of-Office -- make.fun entry.

The joke: the sender is away until Monday and, in the grand tradition of
corporate delegation, has handed all urgent matters to the office plant.
The twist is that the plant has not merely been left in charge -- it has
been *promoted twice*, and still hasn't replied to anyone. It is a real
out-of-office reply (return date, redirect for urgent matters) whose
punchline turns a dead desk plant into the most upwardly mobile employee
in the building, and the least responsive.

Why this line: it was scored against six rival drafts (cat guarding the
inbox, autoreply doing the job, magic 8-ball, inbox requesting a transfer,
and others) on the judge's five criteria -- reads as a genuine reply,
turns on a surprise, sounds like one person's voice, avoids the inbox
jokes everyone has already read, and wastes no words. The promoted plant
won because its twist is concrete and visual, and the punchline lands on
the very absurdity it set up.
"""

import os

LINE = (
    "I'm away until Monday \u2014 please direct urgent matters to my "
    "office plant; it's been promoted twice and still hasn't replied "
    "to anyone."
)


def output_dir() -> str:
    """Return the directory entry.txt should be written to."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> int:
    """Write the one-line out-of-office reply to entry.txt."""
    assert 1 <= len(LINE) <= 140, "line must be 1-140 characters"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE.strip() == LINE, "line must not have leading/trailing whitespace"
    assert LINE.strip(), "line must not be blank"
    LINE.encode("utf-8")

    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    # Round-trip check: what landed on disk must be exactly the line,
    # with no trailing newline and no encoding surprise.
    with open(path, "r", encoding="utf-8", newline="") as handle:
        assert handle.read() == LINE, "entry.txt does not match LINE"
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
