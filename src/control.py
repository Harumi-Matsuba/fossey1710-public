# 対照：鍵（1..9 → a e i o u l m n r）をかき混ぜた1000通りと、本物の鍵を比べる。
# 指標：数字を含む符号のうち、読みが英語の語として通るものの割合。
import sys, random, itertools, lib
random.seed(20261101)
toks=[]
for f in sys.argv[1:]:
    for l in open(f):
        if l.startswith('#'): continue
        for t in lib.tokens(l):
            if any(c.isdigit() for c in t): toks.append(t)
L=list('aeioulmnr')
def score(mapping):
    k=dict(zip('123456789',mapping))
    n=0
    for t in toks:
        d=''.join(k.get(c,c) for c in t)
        if lib.is_word(d): n+=1
    return n
real=score(list('aeioulmnr'))
print(f"数字を含む符号 {len(toks)} 個。本物の鍵で語になる {real}（{100*real/len(toks):.1f}%）")
best=0; ge=0; vals=[]
for i in range(1000):
    p=L[:]; random.shuffle(p)
    s=score(p); vals.append(s)
    if s>=real: ge+=1
    best=max(best,s)
vals.sort()
print(f"かき混ぜ1000回：最大 {best}（{100*best/len(toks):.1f}%）、中央 {vals[500]}、本物以上 {ge}/1000")
