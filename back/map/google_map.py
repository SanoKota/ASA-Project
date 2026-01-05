import os
from typing import Dict, Optional


class GoogleMapAPI:
    """Google Maps APIを扱うクラス"""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        GoogleMapAPIの初期化
        
        Args:
            api_key: Google Maps APIキー。Noneの場合は環境変数から取得
        """
        self.api_key = api_key or os.getenv('GOOGLE_MAPS_API_KEY', '')
        
    def get_api_key(self) -> str:
        """
        APIキーを取得
        
        Returns:
            Google Maps APIキー
        """
        return self.api_key
    
    def get_map_config(self, 
                       center_lat: float = 35.6812, 
                       center_lng: float = 139.7671,
                       zoom: int = 15) -> Dict:
        """
        地図の設定情報を取得
        
        Args:
            center_lat: 地図の中心緯度（デフォルト: 東京駅）
            center_lng: 地図の中心経度（デフォルト: 東京駅）
            zoom: ズームレベル（デフォルト: 15）
            
        Returns:
            地図設定の辞書
        """
        return {
            'api_key': self.api_key,
            'center': {
                'lat': center_lat,
                'lng': center_lng
            },
            'zoom': zoom
        }
    
    def validate_api_key(self) -> bool:
        """
        APIキーが設定されているか確認
        
        Returns:
            APIキーが設定されている場合True
        """
        return bool(self.api_key and self.api_key.strip())
