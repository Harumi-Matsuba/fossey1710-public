# The cipher in Thomas Fossey's notebook of veterinary recipes (1710–1716)

Beinecke Rare Book and Manuscript Library, Yale University, GEN MSS VOL 855.
A notebook of veterinary recipes in which parts of the recipes are written with digits
mixed into the words. This repository records how that writing was read.

**Status: work in progress.** The key has been recovered and checked against clear text
in the same notebook. The transcription of the enciphered passages is not finished, no
reading of the whole is offered yet, and the figures (controls, independent second
transcription, share of the signs that give sense) have not been measured. What is here
is the key, the passage that proves it, and the part read so far.

## The system and the key

The nine commonest letters of English are replaced by the digits; every other letter
stands as it is.

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|
| a | e | i | o | u | l | m | n | r |

Word division, capitals and punctuation are kept. w is written uu, as the notebook
spells it elsewhere (b6455 = blouu = blow).

## How the key is proved

Image 18 of the notebook carries this heading in clear:

> for a blow in a horses eye to eat of y[e] Cell

The second line of cipher on image 19 opens with the same phrase:

> f49 a b6455 38 a h49s2s ey2 → for a blouu in a horses eye

The same phrase thus stands twice in the same hand, once plain and once enciphered.
That fixes 2=e, 3=i, 4=o, 5=u, 6=l, 8=n, 9=r; the next line gives 18d = and and
C9217 = Cream, which fix 1=a and 7=m. The evidence for each value is in `data/key.tsv`.

## Human checking

**No person has checked this transcription.** Both the transcription and the reading
were made by an AI system. Agreement between AI systems is not a substitute for a
person checking the images.

## Use of AI

Finding the item, fetching the images, transcribing, recovering the key and writing
this document were done by an AI system (Anthropic Claude). A person gave the
instructions and decides what is published.

## Contents

- `data/key.tsv` — the key, with the evidence for each value.
- `src/decode.py` — a short program that applies it to a transcription.
- `tests/` — `python3 -m unittest discover -s tests`.
- `docs/METHOD.en.md` — method and limits.
- `docs/OPEN.en.md` — what is still open.
- `docs/PRIOR_CHECK.en.md` — the search for earlier readings.
- `SOURCES.en.md` — the sources.
