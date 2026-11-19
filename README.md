# Wednesday 18 November 2026 — the world's news in one picture

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/irwan11795/makefun-news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/irwan11795/makefun-news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

One-page newspaper front page summarising the world news of Wednesday
18 November 2026: 55 stories, 6 continents — 3 lead stories with drawn
diagrams (Iranian drones over the Gulf, Xi greeting Trump at APEC in
Shenzhen, Voyager 1 one light-day out), 10 more stories in a grid, a
compact world map with numbered pins, a numbered "Also on Wednesday 18 November"
list (stories 14–55) at 15px, a six-number stat strip, and a DATE CHECK box naming
the 17 November stories deliberately left out.

A six-number stat strip on top anchors the day at a glance: 141 drones
fired at Ukraine, Voyager 1 at 25.9bn km, 55 factories shut in Bangladesh,
the EU's €45bn loan for Ukraine, 11,300+ Ebola cases in DR Congo, and
gold settling at $3,742, a 14-month low.

## v3 — elderly-readable revision (19 Nov 2026, user revision)

The user said the bottom of v1 was blurry and asked for more stories and
a page an older person can read. v3: the ALSO list went from 10px to
15px with 18px leading in 3 columns; the map became a compact band
beside the DATE CHECK box instead of eating the whole bottom; story
count rose 42 → 55; grid headlines 13→15px, grid summaries 10→12px,
lead summaries 12→13px, DATE CHECK 10→12px, footer 9→10px. The grid
illustration bands were removed (the decoration that cost the most
space) — each grid cell now has a 5px colour bar; the 3 lead
illustrations stay.

## Entry

`main.py` (Python 3.13, standard library only) copies the pre-rendered
`entry.png` to `/output/entry.png`. No network. The copy is byte-for-byte,
so repeated runs produce identical output — the program prints the SHA-256
of what it wrote so the two runs can be compared.

`entry.png` was drawn by the author with `gen.py` (PIL only, no network,
fully deterministic). See `NOTES.md` for the story list, sources, layout
decisions, and the side-by-side check against the day's top-10 feed.

## Licence

MIT — see `LICENSE`.
