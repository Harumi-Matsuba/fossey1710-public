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
目録はコマごとに「p. 1 [recto]」のような見出しを付けており、読んだ頁についてはその見出しを
`data/pages.tsv` に写す。

画像はこのリポジトリに置かない。上の目録から誰でも取れる。ここで使った取り方は次のとおり。

    https://collections.library.yale.edu/iiif/2/<画像の番号>/full/<幅>,/0/default.jpg

## この作業が答える目録の項目

Daniel Bourdeau の未解決の暗号の目録、項目 **818**
「Thomas Fossey's notebook of veterinary recipes, sections in a vowel-to-digit cipher」。
https://github.com/dbourdeau/cyphersolver

この項目は、Beinecke の目録の注記「Some sections are completed in a cryptographic code」を
引き、DECODE には無いことと、先行が「open（2026年10月28日に確認）」であることを記している。

## 関連

Beinecke の目録に解読文は載っていない。冊子そのものにも解読は書き込まれていない。
