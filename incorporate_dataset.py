import pandas as pd
from functools import reduce

save_path = "dataset/valid"

# 檔案列表
files = [
    f"{save_path}/NVDA.csv",
    f"{save_path}/AAPL.csv",
    f"{save_path}/JPM.csv",
    f"{save_path}/DIS.csv",
    f"{save_path}/XOM.csv"
]
files_wo_prepost = [
    f"{save_path}/NVDA_wo_prepost.csv",
    f"{save_path}/AAPL_wo_prepost.csv",
    f"{save_path}/JPM_wo_prepost.csv",
    f"{save_path}/DIS_wo_prepost.csv",
    f"{save_path}/XOM_wo_prepost.csv"
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
total_df.to_csv(f"{save_path}/total_stock.csv", index=False)
total_df_wo_prepost.to_csv(f"{save_path}/total_stock_wo_prepost.csv", index=False)

print(f"完成:{save_path}/total_stock.csv & total_stock_wo_prepost.csv")