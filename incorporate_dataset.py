import pandas as pd
from functools import reduce

# 檔案列表
files = [
    "dataset/NVDA.csv",
    "dataset/AAPL.csv",
    "dataset/JPM.csv",
    "dataset/DIS.csv",
    "dataset/XOM.csv"
]
files_wo_prepost = [
    "dataset/NVDA_wo_prepost.csv",
    "dataset/AAPL_wo_prepost.csv",
    "dataset/JPM_wo_prepost.csv",
    "dataset/DIS_wo_prepost.csv",
    "dataset/XOM_wo_prepost.csv"
]

dfs = []
dfs_wo_prepost = []


for file in files:
    # 取得股票名稱
    stock_name = file.split("/")[-1].replace(".csv", "")

    # 讀取 CSV
    df = pd.read_csv(file)

    # 欄位重新命名
    df = df.rename(columns={
        "Close": f"{stock_name}_Close",
        "High": f"{stock_name}_High",
        "Low": f"{stock_name}_Low",
        "Open": f"{stock_name}_Open",
        "Volume": f"{stock_name}_Volume"
    })

    dfs.append(df)

for file in files_wo_prepost:
    # 取得股票名稱
    stock_name = file.split("/")[-1].replace("_wo_prepost.csv", "")

    # 讀取 CSV
    df = pd.read_csv(file)

    # 欄位重新命名
    df = df.rename(columns={
        "Close": f"{stock_name}_Close",
        "High": f"{stock_name}_High",
        "Low": f"{stock_name}_Low",
        "Open": f"{stock_name}_Open",
        "Volume": f"{stock_name}_Volume"
    })

    dfs_wo_prepost.append(df)

# 合併資料
total_df = reduce(
    lambda left, right: pd.merge(left, right, on="Datetime", how="outer"),
    dfs
)
total_df_wo_prepost = reduce(
    lambda left, right: pd.merge(left, right, on="Datetime", how="outer"),
    dfs_wo_prepost
)

# 時間排序
total_df = total_df.sort_values("Datetime")
total_df_wo_prepost = total_df_wo_prepost.sort_values("Datetime")

# 存檔
total_df.to_csv("dataset/total_stock.csv", index=False)
total_df_wo_prepost.to_csv("dataset/total_stock_wo_prepost.csv", index=False)

print("完成:dataset/total_stock.csv & total_stock_wo_prepost.csv")