# この手では数字の 9（＝r）と文字の g が同じ形で書かれる。語になる方を採り、該当箇所を一覧にする。
import re, os, glob, itertools, lib

log=open('g9.out.tsv','w'); log.write("file\tbefore\tafter\tdecoded\n"); n=0
import sys
src,dst=sys.argv[1],sys.argv[2]
for f in sorted(glob.glob(src+'/*.txt')):
    lines=open(f).read().split('\n'); out=[]
    for l in lines:
        if l.startswith('#'): out.append(l); continue
        new=l
        for t in lib.tokens(l):
            if lib.is_word(lib.decode(t)): continue
            pos=[i for i,c in enumerate(t) if c in '9g']
            if not pos or len(pos)>4: continue
            cands={}
            for bits in itertools.product('9g',repeat=len(pos)):
                s=list(t)
                for i,b in zip(pos,bits): s[i]=b
                s=''.join(s); d=lib.decode(s)
                if lib.is_word(d): cands[d]=s
            if len(cands)==1:
                d,s=list(cands.items())[0]
                new=re.sub(r'(?<![A-Za-z0-9])'+re.escape(t)+r'(?![A-Za-z0-9])',s,new)
                log.write(f"{os.path.basename(f)}\t{t}\t{s}\t{d}\n"); n+=1
        out.append(new)
    open(os.path.join(dst,os.path.basename(f)),'w').write('\n'.join(out))
log.close(); print('9/g の読み分け',n,'箇所')
