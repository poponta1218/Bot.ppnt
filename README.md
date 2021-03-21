# Bot.ppnt
- 特に何もできないDiscord上で動作するBot

## 機能
- ユーザーが発言した場合にリアクションを返したりメッセージを送信する
- このBotに対してメンションした場合にメッセージを送信する
- 9×9以下のぽぽスイーパー

    ```
    $ps [size] [bomb]
    (sizeは1から9まで，bombはsizeの2乗以下をそれぞれ指定してください．)
    ```


## 構成

### bot_ppnt.py
PythonによるDiscordBotのアプリケーションファイル

### requirements.txt
使用しているPythonのライブラリ情報の設定ファイル

### Procfile
Herokuでのプロセス実行コマンドの設定ファイル

### runtime.txt
Herokuでの実行環境の設定ファイル

### .github/workflows/flake8.yaml
GitHub Actions による自動構文チェックの設定ファイル

### .gitignore
Git管理が不要なファイル/ディレクトリの設定ファイル

### LICENSE
このリポジトリのコードの権利情報

### README.md
このドキュメント
