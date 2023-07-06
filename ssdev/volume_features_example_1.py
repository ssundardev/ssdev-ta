"""This is a example adding volume features.
"""
import pandas as pd
import ta

# Load data
# df = pd.read_csv("../test/data/datas.csv", sep=",")
df = pd.read_csv("C:\\Users\\Lenovo\\Downloads\\dev\\sug-dev\\dev-ta\\ssdev-ta\\test\\data\\datas.csv", sep=",")

# Clean nan values
df = ta.utils.dropna(df)

print(df.columns)

# Add all volume features filling nans values
df = ta.add_volume_ta(df, "High", "Low", "Close", "Volume_BTC", fillna=True)

print(df.columns)
