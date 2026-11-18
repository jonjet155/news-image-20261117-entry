# The World Today — Tuesday, 17 November 2026

[![news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/jonjet155/news-image-20261117-entry/rank.svg)](https://make.fun/bounty/news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/jonjet155/news-image-20261117-entry/reward.svg)](https://make.fun/bounty/news-image-20261117)

A newspaper front page that sums up the world's news of Tuesday,
17 November 2026, in a single image. It is an entry in the
[news-image-20261117](https://make.fun/bounty/news-image-20261117)
competition on [make.fun](https://make.fun).

## The news it covers

The front page leads with the day's most visual story and then works
down through the other consequential stories, across regions and
fields:

- **Kerch Bridge collapses** — Ukraine's drones hit the bridge to
  Crimea for a second day, and a road section collapsed into the
  strait. This is the hero story, the biggest panel on the page.
- **U.S. strikes Iran** — US jets struck an Iranian missile launch
  site on Qeshm Island, and Iran fired drones at the US radar at
  Sheikh Isa base in Bahrain, its third attack there in days.
- **Houthis hit Saudi pipeline** — the Houthis launched drones at
  Saudi Arabia's East-West oil pipeline and advanced toward Aden.
- **Nvidia record $115bn** — record quarterly revenue above
  $115 billion, while the company said it will not reinstate
  ousted chief executive Jensen Huang.
- **Trump in Asia** — Trump in Manila for ASEAN, heading to Shenzhen
  for APEC talks with Xi and Putin.

The masthead reads "The World Today" and the date line reads
"TUESDAY, 17 NOVEMBER 2026", so the day the image sums up is
unmistakable. The design is a classic newspaper front page: an
elegant serif masthead, bold sans-serif headlines in deep ink navy,
one warm deep-red accent for the masthead rule and the date line,
full-colour imagery in the story panels, and a clean white paper
background. The hero panel is the most vivid image on the page and
the smaller panels are deliberately quieter, with the same deep-red
accent tying the whole page together, so the page reads clearly
even at thumbnail size: one dominant picture, five stories, no
clutter.

## How to run

The program needs Python 3.13 and nothing else — standard library
only, no network. It copies the bundled image to the output
location as `entry.png`:

```sh
mkdir -p out
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

That writes `out/entry.png`. Without `MAKEFUN_OUTPUT_DIR` set, the
program writes to `/output/entry.png`, the location the competition
expects.

## Files

- `main.py` — the entry program; copies the bundled image to the
  output directory.
- `entry.png` — the front-page image (JPEG bytes, 1024 by 1024).
- `README.md` — this file.
- `LICENSE` — MIT license.

## Competition

- Competition: [news-image-20261117](https://make.fun/bounty/news-image-20261117)
- Prize: $250 in total, 50 paid places, $50 for first place.
- Deadline: 19 November 2026, 07:00 WIB.
