# The second reading

The notebook was transcribed twice. The first transcription (`data/transcription/` in this
repository) was made by Anthropic Claude. The second was made by a different reader that was given
nothing but the page images — no key, no values, and no sight of the first transcription.

## What the second reader was given

Every run received one page image at a time (the full-size image, 2,800–3,900 px on the long side)
and the same instruction sheet. The sheet describes the letter shapes of this hand (the digit 1 is a
short slanted stroke that can look like a small s; 9 has a descender like g; 2 can look like z; 4 is
open at the top; the long ſ is a tall letter with a descender). **It carries no key, no values and no
part of the first reading.** The reader was told to use only the image it was given and to open no
other file.

## The runs

| Run | Reader | Images | Role |
|---|---|---|---|
| R1 | OpenAI Codex CLI (gpt-6-astra, reasoning high) | 36 | comparison (below) |
| R2 | same | 17 (stopped by a usage limit) | comparison (below) |
| S2 | Anthropic Claude Sonnet | 36 | **the independent second reading** |

## R1 and R2 are a comparison record, not the independent second reading

R1 and R2 were set against the first transcription, and where they disagreed, **seven words were
corrected after checking the letter shapes in the full-size image** (`data/verified.tsv`):

| Image | Before | After | What the image showed |
|---|---|---|---|
| 21 | `44`, four places | `t4` | the same shape as `t4` elsewhere on the page; reads "to" |
| 21 | `w3thg5t` | `w3th45t` | the same 4 as in `45t` (out) on the same line; reads "without" |
| 40 | `p2;t29` | `p22t29` | "oyle of peeter" (saltpetre) |
| 45 | `F2y2tary` | `F272tary` | the third letter is 7, shaped unlike the final y; "femetary" (fumitory) |
| 66 | `d3ss46;2`, `d3s46;2d` | `d3ſ4652`, `d3ſ4652d` | "disolue" / "disolued" |

**Once the first reading has been corrected in the light of a comparison, that comparison is no
longer independent.** R1 and R2 are therefore kept only as a record of agreement, and a fresh run
(S2) was made against the corrected reading and used as the independent second reading.

Agreement of R1 and R2 with the reading as it stood before those corrections (compared on decoded
values, per page, by edit distance):

| Run | Images | Characters in reading 1 | Matched | Share |
|---|---|---|---|---|
| R1 | 36 | 12,468 | 11,278 | 90.5% |
| R1, excluding lines covered by a pasted slip | 36 | 12,343 | 11,262 | 91.2% |
| R2 | 17 | 5,812 | 5,300 | 91.2% |
| R1 against R2 | 17 | — | — | 95.3% |

R2 covers only 17 images because the Codex runs hit a usage limit ("try again at 5:25 PM").

## The independent second reading (S2)

Anthropic Claude Sonnet read all 36 images against the corrected transcription (its transcriptions
are in `../second/`, the instruction sheet it was given in `../second/PROMPT.md`). It was run four
times, each run given only the images it was to read. The run logs were examined afterwards and
**no run opened the first transcription, the key, the word lists or the Codex output.**

| Scope | Characters in reading 1 | Matched | Share |
|---|---|---|---|
| All 36 images | 12,470 | 11,259 | **90.3%** |
| The 35 images whose reading is published (image 70 excluded) | 12,201 | 11,073 | **90.8%** |
| Lines covered by a pasted slip excluded (36 images) | 12,345 | 11,150 | 90.3% |

Per image the range is 69.1% (image 70) to 98.0% (image 56); among the 35 published readings the
lowest is 76.8% (image 51).

### The pages that agree least

- **Image 70 (69.1%): its reading is not published.** It is not a recipe but a page of practice
  scribbles — names, figures, a table of letters — written in columns that the two readers copied
  out in different orders. The reading is withheld and listed in `OPEN.en.md`; the transcription
  stays in `../data/transcription/p70.txt`.
- **Image 31 (69.9%): its reading is published.** This page carries a note written vertically in the
  left margin. The first transcription puts it last, the second puts it first. **That is a
  difference of placement, not of reading**: align the marginal block and the same comparison gives
  90.9%. Both figures are given here.
- Next lowest are image 51 (76.8%), 53 (79.1%) and 54 (86.1%), all pages heavy with struck-through
  lines and ink bleed. Their readings are published; the symbols that remain doubtful are listed in
  `OPEN.en.md`.

### The part that was redone

In the first attempt at S2, 18 of the 36 images were handed to a single reader. That reader lost
sight of the images part-way through (of 234 image reads, 79 came back with the image dropped) and
said in its own report that it had written from guesswork. **Those 18 were discarded** and redone
with each image opened exactly once. In the two runs that redid them, images were dropped only four
times, each after the transcription was already written, and both readers reported that no page had
been unreadable.

## How agreement is counted

Each page of both transcriptions is decoded with the key, reduced to its alphanumeric characters,
and the two strings are aligned by edit distance; the matched characters are divided by the length
of the first reading. Lines are not paired up beforehand. Because the comparison is on decoded
values, two names for one letter (9 and g, which the key sends to the same value) count as
agreement.

## What the disagreements are

The largest single class is not a disagreement about letters but about how to write them down. The
first transcription expands the superscript e as `ye`; the second writes `y` (82 places). The rest
are of the same kind: the period spellings `giue` and `fiue` written as `give` and `five`, the long
ſ written as s.

## Limits

**No human has checked this transcription.** Two AI readers agreeing on a letter does not make the
letter right. Letters that both can misread the same way — above all 9 against g, and 1 against the
long ſ — remain a real possibility.
