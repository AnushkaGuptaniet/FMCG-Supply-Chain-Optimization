import pandas as pd

df = pd.read_csv("dataset/clean_fmcg.csv")

df["Date"] = pd.to_datetime(df["Date"])

# Date Features
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day

# Demand Category
df["Demand_Category"] = pd.qcut(
    df["Sales_Quantity"],
    q=3,
    labels=["Low","Medium","High"]
)

print(df[["Sales_Quantity","Demand_Category"]].head())

df.to_csv(
    "dataset/feature_engineered_fmcg.csv",
    index=False
)

print("Feature Engineering Completed")