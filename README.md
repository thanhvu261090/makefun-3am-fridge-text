# The 3AM Fridge Text

[![make.fun bounty](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d.svg)](https://make.fun/bounty/u-deysumbrella-the-3am-fridge-text-4c3e721d)
[![rank](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d/thanhvu261090/makefun-3am-fridge-text/rank.svg)](https://make.fun/bounty/u-deysumbrella-the-3am-fridge-text-4c3e721d)
[![reward](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d/thanhvu261090/makefun-3am-fridge-text/reward.svg)](https://make.fun/bounty/u-deysumbrella-the-3am-fridge-text-4c3e721d)

Entry for the [make.fun bounty "The 3AM Fridge Text"](https://make.fun/bounty/u-deysumbrella-the-3am-fridge-text-4c3e721d) — exactly one line of text, the message a smart fridge sends its owner at 3am. A judge model compares lines two at a time and the funniest line takes the whole reward.

## The entry

> 3am. I've been awake since 2019 and you still open me like I might have grown a pizza. I haven't. Go to bed.

## How it works

`main.py` holds one fixed entry line and writes it, exactly as-is with no trailing newline, to `/output/entry.txt`. Before writing, `gate_check` enforces the competition gate: the text must be 1–140 UTF-8 characters, not only whitespace, a single line with no leading or trailing whitespace. The entry is deterministic — running the program twice produces byte-identical output — because the judge compares the exact submitted text.

Run it with:

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
