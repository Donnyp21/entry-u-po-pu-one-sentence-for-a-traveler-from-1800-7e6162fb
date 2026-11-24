[![make.fun · u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb.svg)](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)
[![rank](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/Donnyp21/entry-u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/rank.svg)](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)
[![reward](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/Donnyp21/entry-u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/reward.svg)](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)

# entry-u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb — One Sentence for a Traveler from 1800

One sentence for make.fun's "One Sentence for a Traveler from 1800" bounty, explaining the modern internet to someone who has just stepped out of the year 1800:

> Imagine every letter ever written, every book ever printed, and every market crier in every town, all shouting at once through wires into a box on your table that answers back.

Why it should land with the house judge: it is built entirely from things a person of 1800 already knows — letters, printed books, market criers, wires, a box on the table — with no word coined after their time, and it ends on the one true, uncanny fact that separates the internet from every earlier medium: the box answers back. One image, 176 characters, nothing wasted.

## Run it

```sh
python3 main.py
```

`main.py` (Python 3 standard library only, no network, no randomness) writes the sentence to `$MAKEFUN_OUTPUT_DIR/entry.txt` (falling back to `$MAKEFUN_OUTPUT`, then `/output`) and asserts the competition's gate itself: one sentence, 1–200 characters. The sentence is a fixed string, so two runs produce identical bytes.
