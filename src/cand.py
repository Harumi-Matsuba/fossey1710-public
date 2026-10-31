# 語に通らない符号について、この手で紛らわしい字（1↔s、9↔g、d↔0 など）を入れ替えた候補のうち、語になるものを出す。
import sys, itertools, lib
PAIRS={'1':'s','s':'1','9':'g','g':'9','S':'1','0':'d','c':'e','e':'c','t':'f','f':'t'}
def cands(tok):
    pos=[i for i,c in enumerate(tok) if c in PAIRS]
    out=[]
    for r in range(1,min(len(pos),4)+1):
        for sel in itertools.combinations(pos,r):
            s=list(tok)
            for i in sel: s[i]=PAIRS[tok[i]]
            s=''.join(s)
            if lib.is_word(lib.decode(s)): out.append((s,lib.decode(s)))
    return out
for f in sys.argv[1:]:
    for i,l in enumerate(open(f),1):
        if l.startswith('#'): continue
        for t in lib.tokens(l):
            d=lib.decode(t)
            if lib.is_word(d): continue
            c=cands(t)
            print(f.split('/')[-1], i, t, d, ' | '.join(f'{a}={b}' for a,b in c[:4]) or '-', sep='\t')
