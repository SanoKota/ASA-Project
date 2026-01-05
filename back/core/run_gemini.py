import os
import pandas as pd
from dotenv import load_dotenv
from typing import Type, List
from pydantic import BaseModel
from core.create_math import createdifferential, createintegral, USER_PROMPT
import io

# APIキーを使用してGemini APIを設定
import google.generativeai as genai

def run_gemini() -> pd.DataFrame:
    """
    Gemini APIを使用してコンテンツを生成する関数。
    Return:
        pd.DataFrame, geminiの出力結果
    """
    # .envファイルのパスを明示的に指定
    load_dotenv()

    # 環境変数からAPIキーを取得
    api_key = os.getenv("GOOGLE_API_KEY")

    if api_key:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('models/gemini-2.5-pro')
        response = model.generate_content([
            {"text": SYSTEM_PROMPT},
            {"text": USER_PROMPT}
        ])
        # DataFrameで返す
        return response
    else:
        print("APIキーが設定されていません。")
        return pd.DataFrame()


if __name__ == "__main__":
    df = run_gemini()