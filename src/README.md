# プログラムの使い方

- `decode.py <書き起こしのファイル>` — 鍵で読む。
- `ratio.py ../data/transcription/*.txt` — 意味の通る割合を測る。
- `control.py ../data/transcription/*.txt` — 鍵をかき混ぜた1000通りとの対照。
- `cand.py <ファイル>` — 語にならない符号について、この手で紛らわしい字を入れ替えた候補を出す（直しの候補を挙げるだけ。採否は画像で決める）。
- `g9.py <入力の folder> <出力の folder>` — 数字の 9 と文字の g が同じ形のため、語になる方を採る。
- `lib.py` — 共通。語の判定に、英語の辞書（/usr/share/dict/words。macOS に付属。無い環境では
  Webster's Second International の見出し語の一覧を同じ場所に置く）と、`../data/plain_vocab.txt`、
  `../data/materia.txt` を使う。
