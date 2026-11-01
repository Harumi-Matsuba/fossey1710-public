# 1回目の書き起こしと、2回目の読み手の書き起こしの一致率を測る。
# 使い方: python3 src/agreement.py <2回目のフォルダ>        例: python3 src/agreement.py second/sonnet
#         python3 src/agreement.py second/fable p70        1 枚だけを測る
#
# どちらも鍵で読んだ値の英数字列にしてから、編集距離で突き合わせ、
# 一致した文字数を1回目の文字数で割る。行の対応は付けない（①順そのまま）。
# ②順を無視：1回目の各行に、相手の行のうち最も合うものを1対1で割り当てて足す。
# ①と②の差が、写した順の違いで説明できる分の上限になる。
import sys, os, re, glob, difflib, lib

def lines(path):
    out = []
    for l in open(path):
        if l.startswith('#'):
            continue
        l = re.sub(r'\[[^\]]*\]', '', lib.strip_marks(l))
        s = ''.join(c for c in lib.decode(l) if c.isalnum()).lower()
        if s:
            out.append(s)
    return out

def match(a, b):
    return sum(x.size for x in difflib.SequenceMatcher(None, a, b, autojunk=False).get_matching_blocks())

def ordered(a, b):
    A, B = ''.join(a), ''.join(b)
    return len(A), match(A, B)

def order_free(a, b):
    pairs = sorted(((match(x, y), i, j) for i, x in enumerate(a) for j, y in enumerate(b)), reverse=True)
    doneA, doneB, same = [False]*len(a), [False]*len(b), 0
    for m, i, j in pairs:
        if m == 0:
            break
        if doneA[i] or doneB[j]:
            continue
        doneA[i] = doneB[j] = True
        same += m
    return sum(len(x) for x in a), same

folder = sys.argv[1]
only = sys.argv[2] if len(sys.argv) > 2 else None
tot = same = 0
for f in sorted(glob.glob('data/transcription/p*.txt')):
    name = os.path.basename(f)[:-4]                 # p70
    if only and name != only:
        continue
    g = os.path.join(folder, 'f' + name[1:] + '.txt')
    if not os.path.exists(g):
        continue
    a, b = lines(f), lines(g)
    t1, m1 = ordered(a, b)
    t2, m2 = order_free(a, b)
    tot += t1
    same += m1
    print(f"{name}\t①順そのまま {m1}/{t1}＝{100*m1/t1:.1f}%\t②順を無視 {m2}/{t2}＝{100*m2/t2:.1f}%")
if tot:
    print(f"合計：{same}/{tot}＝{100*same/tot:.1f}%")
