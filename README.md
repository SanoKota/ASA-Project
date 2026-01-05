# ASA-Project
アウトドアサークルで使える便利機能を詰め込んだアプリ開発

## 機能
- Google Maps APIを使用した地図表示機能
- FlaskベースのWebアプリケーション

## セットアップ

### 1. 依存パッケージのインストール
```bash
pip install -r requirements.txt
```

### 2. Google Maps APIの設定
- [Google Cloud Console](https://console.cloud.google.com/)でプロジェクトを作成
- Maps JavaScript APIを有効化
- APIキーを作成
- 環境変数を設定:
```bash
export GOOGLE_MAPS_API_KEY="YOUR_GOOGLE_MAPS_API_KEY"
```

### 3. アプリケーションの起動
```bash
cd front
python app.py
```

ブラウザで `http://localhost:5000` にアクセスしてください。

## 実行例
Flaskアプリケーションを起動すると、Google Mapsが組み込まれたWebページが表示されます。
デフォルトでは東京駅を中心とした地図が表示されます。

## Gemini APIについて
### APIの設定：
- 各自で以下のURL先からGemini APIを取得
`https://ai.google.dev/gemini-api/docs?hl=ja`
- ".env"という名前でファイルを作成、ファイル内には以下の行を追加する
`GOOGLE_API_KEY = "YOUR_API_KEY"`