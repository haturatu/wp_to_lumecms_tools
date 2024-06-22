# wp_to_lumecms_tools

Before proceeding, please export your WordPress content to Markdown format using the following tool:

[WordPress Export to Markdown](https://github.com/lonekorean/wordpress-export-to-markdown)

Please note that this process requires manual intervention and cannot be fully automated. Assistance through Linux commands is recommended.

## coverchange.py
```
python coverchange.py /your/dir
```

If LumeCMS doesn't support thumbnails, lines like `coverImage: "Thisimage.jpg"` will be ignored. Therefore, images in the content should be displayed in Markdown format at the beginning of the line, like `![Thisimage.jpg](/uploads/Thisimage.jpg)`. Since the image directory in LumeCMS can vary by user, modify the relevant code accordingly. Afterwards, if the images are in a directory named "images" as shown below:

```
├── 遊びの仮想neofetch
│   ├── Play Virtual Neofetch.md
│   └── images
│       ├── miku-1024x1024.jpg
│       ├── miku.jpg
│       ├── teto-1024x1024.png
│       └── teto.png
```

Move this file to the LumeCMS images directory using the `file` command and `mv`.

Do not delete the `*coverImage: "Thisimage.jpg"*` string as it appends the Markdown format every time the script is executed. Always backup and execute once.

## transname.py
```
python transname.py
```

Use the Deep Translator ([Deep Translator](https://github.com/prataffel/deep_translator)) to translate directory names as follows:

```
├── 無能がが答える-あなたの好きなモノについて１０
│   └── index.md
├── 無能のログイン機能実装をしたけど
│   └── index.md
├── 無料サーバー、wkey-meの思い出
│   └── index.md
├── 遊びの仮想neofetch
│   ├── images
│   └── index.md
└── 連続したテキストからyoutube-url抜くだけでの正規表現grep
    └── index.md
```

Rename the directories to English and rename `index.md` accordingly:

```
├── 無能がが答える-あなたの好きなモノについて１０
│   └── Incompetent answers - 10 things you like.md
├── 無能のログイン機能実装をしたけど
│   └── I implemented a useless login function.md
├── 無料サーバー、wkey-meの思い出
│   └── Memories of the free server, wkey-me.md
├── 遊びの仮想neofetch
│   ├── Play Virtual Neofetch.md
│   └── images
└── 連続したテキストからyoutube-url抜くだけでの正規表現grep
    └── Regular expression grep to extract youtube-url from continuous text.md
```

Then, move this file to the LumeCMS posts directory using the `file` command and `mv`.

