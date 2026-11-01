# 共通：鍵で読む・語に通るかを見る。
import re, unicodedata
KEY={'1':'a','2':'e','3':'i','4':'o','5':'u','6':'l','7':'m','8':'n','9':'r'}
WORDS=set(w.strip().lower() for w in open('/usr/share/dict/words'))
WORDS|=set(w.strip().lower() for w in open('/usr/share/dict/propernames'))
# 当時の薬・処方でよく出る語と綴り（手帳の平文の頁に出るもの）
try:
    import os
    _here=os.path.dirname(os.path.abspath(__file__))
    for _d in (_here, os.path.join(_here,'..','data')):
        try:
            WORDS|=set(w.strip().lower() for w in open(os.path.join(_d,'plain_vocab.txt')) if w.strip())
            WORDS|=set(l.split('\t')[0].strip().lower() for l in open(os.path.join(_d,'materia.txt')) if l.strip() and not l.startswith('#'))
        except FileNotFoundError:
            pass
except FileNotFoundError:
    pass
WORDS|=set('''ye yt wth oz pint pints quart quarts handfull handfulls spoonfull spoonfulls
treacle venice turpentine bole armenick armeniack armery allom allum sallet sallad linseed
hogsland hogslard lard mallows mallowes camomile elder eldern wormwood rue garlick garlicke
brimstone nittre nitter saltpeter sheeps sheep oyle oile oyl hony honey vinegar verjuice varges
cankers canker swelling swellings bruised cordiall drench drinke drinck morning knight night
approved received medcen medcine medicin physick bullocks buddocks burdocks bugloss'''.split())
# 当時の綴りの揺れ：uu=w、u/v・i/j の通用、語尾の e、ck/k、二重字
SUF=("s","es","'s","'d","ed","d","ing","eth","th","est","er")
def base_forms(w):
    out={w}
    for suf in SUF:
        if w.endswith(suf) and len(w)-len(suf)>=2:
            b=w[:-len(suf)]; out|={b,b+'e',b[:-1] if len(b)>2 and b[-1]==b[-2] else b}
    return out

def variants(w):
    w=w.lower(); out=set(base_forms(w))
    for s in list(out):
        out|=set().union(*[base_forms(x) for x in (s.replace('uu','w'),s.replace('u','v'),s.replace('v','u'),s.replace('i','j'),s.replace('ou','o'),s.replace('oo','ou'))])
    more=set()
    for s in out:
        more|={s, s+'e', s.rstrip('e'), s.replace('ck','k'), s.replace('ll','l'), s.replace('ss','s'),
               s.replace('oo','o'), s.replace('ee','e'), s.replace('yn','ine'), s.replace('y','i'),
               re.sub(r'e$','',s)+'ed'}
    return more
def is_word(w):
    w=w.replace('ſ','s').replace('ʃ','s')   # 長い s は文字の s
    w=re.sub(r"[^A-Za-z]","",w)
    if len(w)<=1: return w.lower() in ('a','i','o')
    return any(v in WORDS for v in variants(w))
def decode(s):
    return ''.join(KEY.get(c,c) for c in s)
def strip_marks(line):
    line=re.sub(r'\[del:([^\]]*)\]',r'\1',line)   # 消された文も記号として数える
    line=re.sub(r'\[[^\]]*\]','',line)              # [貼り紙で見えず] などの注記は外す
    line=re.sub(r'[{}]','',line)
    return line
def tokens(line):
    # 「…」の付いた符号は、貼り紙で切れた断片。語にならないのが当たり前なので数えない。
    out=[]
    for t in re.split(r"[^A-Za-z0-9'ſ…]+", strip_marks(line)):
        if not t or '…' in t: continue
        out.append(t)
    return out


def page_tokens(path):
    """頁のファイルから、行またぎの語をつないだ符号の並びを返す（(行番号, 符号) の列）。"""
    ls=[l for l in open(path) if not l.startswith('#')]
    out=[]; SKIP=set()
    for i,l in enumerate(ls):
        toks=tokens(l)
        # 同じ行で、語が2つに分かれて書かれている所（例「19771 83ck」＝armmaniack）はつなぐ
        j=0; merged=[]
        while j<len(toks):
            if (j+1<len(toks) and not is_word(decode(toks[j]))
                    and is_word(decode(toks[j]+toks[j+1]))):
                merged.append(toks[j]+toks[j+1]); j+=2
            else:
                merged.append(toks[j]); j+=1
        toks=merged
        nxt=tokens(ls[i+1]) if i+1<len(ls) else []
        if toks and nxt and is_word(decode(toks[-1]+nxt[0])) and (
                not is_word(decode(toks[-1])) or not is_word(decode(nxt[0]))):
            toks=toks[:-1]+[toks[-1]+nxt[0]]
            SKIP.add((i+1,nxt[0]))
        for t in toks:
            if (i,t) in SKIP: continue
            out.append((i,t))
    return out

def bad_tokens(path):
    return [(i,t) for i,t in page_tokens(path)
            if any(c.isdigit() for c in t) and not is_word(decode(t))]
