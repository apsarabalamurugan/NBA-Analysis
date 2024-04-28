import os

import pandas as pd
from tqdm import tqdm

csv_files = os.listdir("data")
csv_files = sorted(csv_files)

if "pbpALL.csv" in csv_files:
    csv_files.remove("pbpALL.csv")

df_list = []

for csv_name in tqdm(csv_files):
    try:
        df = pd.read_csv(f"data/{csv_name}", encoding="utf8")
        df_list.append(df)
    except Exception as e:
        print("Something went wrong: ", e)

full_df = pd.concat(df_list, ignore_index=True)

full_df.to_csv("data/pbpALL.csv", index=False)
