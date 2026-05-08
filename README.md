# 1.程式說明
yfinance_crawler.py:從yahoo finance 抓取資料  
incorporate_dataset.py:將yfinance_crawler.py 抓的資料合併成一個csv
# 2.Dataset 說明
## 公司名代號  
1.AAPL:apple  
2.NVDA:NVIDIA  
3.JPM:摩根大通(金融)  
4.XOM:ExxonMobil(傳統油氣)  
5.DIS:迪士尼  
## 快速區分 Dataset
XX.csv: 包含盤前盤後的資料  
XX_wo_prepost.csv: 只有開盤的資料  
total_XX: 所有股票資料的總和
# 3.其他
1.OHLCV 代表金融交易中常用的開盤價 (Open)、最高價 (High)、最低價 (Low)、收盤價 (Close) 和 成交量 (Volume)，是技術分析的基礎。  
2.Dataset 時間範圍  
train:2025-01-01~2025-12-31.  
valid:2026-01-01~2026-02-28.  
3.資料量：  
train:total_stock.csv(4100多筆)、total_stock_wo_prepost.csv(1700多筆)  
valid:total_stock.csv(600多筆)、total_stock_wo_prepost.csv(200多筆)  
