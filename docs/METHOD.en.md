# Method

## 1. Choosing the item

From Daniel Bourdeau's catalogue of unsolved ciphers (849 entries), items were taken
whose images are public, which need no visit to the archive, and which nobody has
worked on. Entry 818 (Fossey's notebook) is one of them. The search for earlier
readings is in `PRIOR_CHECK.en.md`.

## 2. Images

Fetched from Yale's public IIIF endpoint without an account. All 76 images were first
taken at 800 px wide to find the enciphered pages; those pages were then taken again at
1600 px, and the page that proves the key also at full size (3885 px on the long side).
Two seconds were left between requests. No image is reproduced in this repository.

## 3. Recovering the key

Only the digits 1–9 occur; 0 never does. The digits stand inside otherwise English
words, so they are letters. The heading on image 18 and the second line of cipher on
image 19 are the same phrase, which fixes seven values at once; the next two words fix
the remaining two. The evidence for each value is in `data/key.tsv`.

There is no 0 because the nine digits were given to nine letters; quantities in the
recipes ("one ounce") are spelled out.

## 4. Transcription

Each line is cropped from the page image and copied one character at a time. In this
hand the digit 1 and the long s, 9 and the long s, and 2 and 1 are easily confused.
Doubtful characters are written as ? and resolved by taking the reading that gives an
English word; those places are marked in the reading files.

## 5. Limits

- No person has checked this transcription.
- The spelling is of its time and many words are not in a modern word list (uu for w,
  ck for k, a final e added or dropped). Any count of words that make sense must allow
  for this.
- The transcription is not finished, so no controls, no independent second transcription
  and no share of signs that give sense are offered yet.
