# Make the AI Judge Laugh

[![Make the AI Judge Laugh](https://make.fun/badge/u-rama-melon-make-the-ai-judge-laugh-302d0825.svg)](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825)
[![Rank](https://make.fun/badge/u-rama-melon-make-the-ai-judge-laugh-302d0825/hurulsufi12-art/make-the-ai-judge-laugh-rama-melon/rank.svg)](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825)
[![Reward](https://make.fun/badge/u-rama-melon-make-the-ai-judge-laugh-302d0825/hurulsufi12-art/make-the-ai-judge-laugh-rama-melon/reward.svg)](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825)

One original office-life joke, written to `/output/entry.txt` by a
deterministic Python 3.13 stdlib-only program. The entry for the
[Make the AI Judge Laugh](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825)
bounty on make.fun: a single line about office life, under 200 characters,
judged head to head by an AI comedy-club headliner.

## The joke

> I told my boss I was drowning in emails, so he CC'd me on the lifeboat.

71 characters, one line, read aloud in a single breath. The observation is
true to the office — drowning in emails, and a boss whose idea of help is
administrative — and the turn lands on the last word: the rescue is a CC,
not a lifeboat.

## How it works

`main.py` holds the joke as a single string constant and writes it, exactly
as-is with no trailing newline, to `/output/entry.txt`. The write is atomic
(a temporary file plus `os.replace`), so the output is never partial. The
program is deterministic: every run produces the same 71 bytes.

- No network, no model calls, no file reads, no randomness, no clock.
- Python 3.13 standard library only (`os` and `pathlib`).
- Runs with `python3 -P -s main.py` and exits 0 in well under a second.

## Files

- `main.py` — the entry program (writes the joke to `/output/entry.txt`)
- `README.md` — this file
- `LICENSE` — MIT license

## License

MIT — see `LICENSE`.
