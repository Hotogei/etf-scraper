import requests
import pandas as pd
from datetime import date

def fetch_etf_holdings(etf_code="00981A"):
    """
    抓取主動式 ETF 成分股與持股變動資料
    """
    # 請將下方 URL 替換為您從 F12 Network 撈取出來的真實 API 接口或資料連結
    api_url = f"https://api.cmoney.tw/etf/tw/{etf_code}/fundholding" 
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'application/json, text/javascript, */*; q=0.01'
    }
    
    print(f"開始抓取 {etf_code} 資料...")
    
    try:
        response = requests.get(api_url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            # 假設該網站回傳的是 JSON 格式
            data = response.json()
            
            # 將資料轉換為 DataFrame (請依實際 JSON Key 值做調整)
            # df = pd.DataFrame(data.get('holdings', [])) 
            
            # --- 測試階段的偽資料結構範例 ---
            dummy_data = [
                {'代號': '2330', '名稱': '台積電', '持股比例': '35.12%', '增減張數': '+346'},
                {'代號': '6187', '名稱': '萬潤', '持股比例': '5.45%', '增減張數': '+684'}
            ]
            df = pd.DataFrame(dummy_data)
            # --------------------------------
            
            # 加入更新日期欄位
            df['抓取日期'] = date.today().strftime('%Y-%m-%d')
            
            # 儲存為 CSV 檔案
            filename = f"{etf_code}_holdings_{date.today().strftime('%Y%m%d')}.csv"
            df.to_csv(filename, index=False, encoding='utf-8-sig')
            
            print(f"成功！資料已儲存至：{filename}")
            print(df.head())
            return df
            
        else:
            print(f"連線失敗，狀態碼：{response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"發生連線錯誤：{e}")

if __name__ == '__main__':
    fetch_etf_holdings("00981A")