# 資料

## 原本

Beinecke Rare Book and Manuscript Library, Yale University、**GEN MSS VOL 855**
「Notebook of veterinary recipes : manuscript」1710〜1716年。

- 目録：https://collections.library.yale.edu/catalog/33569870
- IIIF の目録：https://collections.library.yale.edu/manifests/33569870
- 76 コマ、全部が電子化され、公開されている。

持ち主は **Thomas Fossey** と署名している（コマ 5「Thomas Fossey 1716」）。処方の末尾に
「Approved by me Tho: Fossey」「Ed. Fossey approved」とあるものが複数ある。見返しには
William Edward・William Feniel の名もある。

コマの番号は IIIF の目録の番号（1〜76）で示す。冊子自身の頁付けは一部にしかないため。

暗号の数字が出るのは次の 38 コマ：
6・19・21・23・25・27・28・29・30・31・32・33・34・36・40・41・43・44・45・47・49・51・53・54・55・56・57・
59・60・61・62・63・64・65・66・67・69・70。
このうち 29・30 は、25〜34 と同じ見開きを、貼り紙の位置だけ変えて撮ったもので、
そこでしか見えない暗号の行は無かった（確かめた）。

画像はこのリポジトリに置かない。上の目録から誰でも取れる。ここで使った取り方は次のとおり。

    https://collections.library.yale.edu/iiif/2/<画像の番号>/full/<幅>,/0/default.jpg
    https://collections.library.yale.edu/iiif/2/<画像の番号>/full/full/0/default.jpg   （原寸）

## この作業が答える目録の項目

Daniel Bourdeau の未解決の暗号の目録、項目 **818**
「Thomas Fossey's notebook of veterinary recipes, sections in a vowel-to-digit cipher」。
https://github.com/dbourdeau/cyphersolver

先行との関係は `docs/PRIOR_CHECK.md` に書いた（着手前 2026年10月31日、公表前 2026年11月1日）。

## 語彙の典拠

読みが語として通るかの判定に使った語彙は3つ。
1. 英語の辞書（macOS の /usr/share/dict/words、Webster's Second International の見出し語）。
2. この手帳の平文の頁に出る綴り（`data/plain_vocab.txt`）。
3. 当時の薬材・単位の名（`data/materia.txt`。1件ずつ、この手帳のどのコマで字を確かめたか、
   または当時の獣医・薬の書で普通に使う名であることを書いた）。
