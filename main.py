"""Make the AI Judge Laugh — one original office-life joke.

Writes the joke to /output/entry.txt: exactly the 71-character text,
UTF-8, one line, no trailing newline. Python 3.13 stdlib only,
deterministic, no network, no model call, no file reads.

No trailing newline is deliberate: the exact tie-break in RULES.txt
favours the smaller text in bytes, so the file is exactly 71 bytes.
"""

import os
from pathlib import Path

# 71 characters, 71 bytes (pure ASCII), one line, no trailing newline.
JOKE = "I told my boss I was drowning in emails, so he CC'd me on the lifeboat."


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    tmp = out.with_suffix(".tmp")
    tmp.write_text(JOKE, encoding="utf-8")
    os.replace(tmp, out)


if __name__ == "__main__":
    main()
