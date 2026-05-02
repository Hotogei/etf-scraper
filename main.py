import pandas as pd
from datetime import datetime

def fetch_etf_data():
    # 模擬抓取 ETF 00981A 的成分股調整資料 (可根據您的需求修改爬蟲邏輯)
    data = {
        "代碼": ["6187", "3711", "2313", "3037", "8996", "2330", "5274", "1303", "7769"],
        "股票名稱": ["萬潤", "日月光投控", "華通", "欣興", "高力", "台積電", "信驊", "南亞", "鴻勁"],
        "張數": ["+684", "+1,323", "+1,200", "+939", "+379", "+346", "+52", "-1,374", "-98"],
        "備註": ["新進", "", "", "", "", "", "", "出清", "出清"]
    }
    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 開始抓取 ETF 00981A 成分股調整資料...")
    
    # 取得資料
    df_etf = fetch_etf_data()
    
    # 印出資料確認正確性
    print("\n--- 抓取到的 ETF 數據 ---")
    print(df_etf)
    print("-------------------------\n")
    
    # 儲存資料為 CSV 檔案 (加入 utf-8-sig 讓 Excel 開啟時不會亂碼)
    output_filename = "etf_00981A_adjustment.csv"
    df_etf.to_csv(output_filename, index=False, encoding='utf-8-sig')
    
    print(f"資料已成功寫入至檔案：{output_filename}")