"""Decode the vowel-to-digit cipher of Thomas Fossey's notebook of veterinary recipes
(Beinecke Rare Book and Manuscript Library, Yale University, GEN MSS VOL 855, 1710-1716).

The cipher replaces the nine commonest letters of English by the digits 1-9 and leaves
every other letter standing:

    1=a  2=e  3=i  4=o  5=u  6=l  7=m  8=n  9=r

Usage:  python3 decode.py <transcription file> [...]
        python3 decode.py -        (read from standard input)

Lines beginning with '#' are passed through unchanged.
"""
import sys

KEY = {'1': 'a', '2': 'e', '3': 'i', '4': 'o', '5': 'u',
       '6': 'l', '7': 'm', '8': 'n', '9': 'r'}


def decode(text):
    """Replace cipher digits by their letters; leave everything else as it stands."""
    return ''.join(KEY.get(ch, ch) for ch in text)


def decode_stream(lines):
    for line in lines:
        line = line.rstrip('\n')
        yield line if line.startswith('#') else decode(line)


def main(argv):
    names = argv[1:] or ['-']
    for name in names:
        src = sys.stdin if name == '-' else open(name, encoding='utf-8')
        try:
            for out in decode_stream(src):
                print(out)
        finally:
            if src is not sys.stdin:
                src.close()


if __name__ == '__main__':
    main(sys.argv)
