# 意味の通る割合：暗号の記号＝数字1〜9 の出現のうち、
# その数字を含む符号の読みが語として通るものの割合。
import sys, lib
# 行またぎの語（行末と次行の頭がつながる）を、つないだ形で数える
tot=ok=0; bad={}
for f in sys.argv[1:]:
    for _i,t in lib.page_tokens(f):
        if True:
            n=sum(c.isdigit() for c in t)
            if not n: continue
            tot+=n
            if lib.is_word(lib.decode(t)): ok+=n
            else: bad[t]=bad.get(t,0)+n
print(f"暗号の記号 {tot}、語として通る {ok}（{100*ok/tot:.1f}%）")
for t,n in sorted(bad.items(),key=lambda x:-x[1])[:25]: print(n,t,lib.decode(t),sep='\t')
