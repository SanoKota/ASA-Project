import sys
import os
from flask import Flask, render_template, jsonify

# バックエンドのモジュールをインポートできるようにパスを追加
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from back.map.google_map import GoogleMapAPI

app = Flask(__name__)

# Google Maps APIの初期化
google_map = GoogleMapAPI()


@app.route('/')
def index():
    """メインページを表示"""
    # APIキーが設定されているか確認
    if not google_map.validate_api_key():
        return render_template('error.html', 
                             error_message="Google Maps APIキーが設定されていません。環境変数 GOOGLE_MAPS_API_KEY を設定してください。")
    
    # 地図の設定を取得（東京駅を中心に表示）
    map_config = google_map.get_map_config(
        center_lat=135.6812,  # 東京駅の緯度
        center_lng=139.7671,  # 東京駅の経度
        zoom=15
    )
    
    return render_template('index.html', map_config=map_config)


@app.route('/api/map-config')
def get_map_config():
    """地図設定をJSON形式で返すAPI"""
    if not google_map.validate_api_key():
        return jsonify({'error': 'APIキーが設定されていません'}), 400
    
    map_config = google_map.get_map_config()
    return jsonify(map_config)


@app.route('/health')
def health():
    """ヘルスチェック用エンドポイント"""
    return jsonify({'status': 'ok', 'api_key_set': google_map.validate_api_key()})


if __name__ == '__main__':
    # デバッグモードで起動
    app.run(debug=True, host='0.0.0.0', port=5000)
