# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Load cleaned dataset
# df = pd.read_csv("dataset/clean_fmcg.csv")

# print(df.head())

# # Create reports folder if it doesn't exist
# import os

# # -----------------------------
# # 1. Sales Quantity Distribution
# # -----------------------------
# plt.figure(figsize=(8,5))
# sns.histplot(df["Sales_Quantity"], bins=30)
# plt.title("Sales Quantity Distribution")
# plt.savefig("reports/sales_distribution.png")
# plt.show()

# # -----------------------------
# # 2. Inventory Distribution
# # -----------------------------
# plt.figure(figsize=(8,5))
# sns.histplot(df["Inventory_Level"], bins=30)
# plt.title("Inventory Level Distribution")
# plt.savefig("reports/inventory_distribution.png")
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("dataset/clean_fmcg.csv")

# Sales Distribution
plt.figure(figsize=(8,5))
sns.histplot(df["Sales_Quantity"], bins=30)
plt.title("Sales Quantity Distribution")
plt.savefig("reports/sales_distribution.png")
plt.show()

# Inventory Distribution
plt.figure(figsize=(8,5))
sns.histplot(df["Inventory_Level"], bins=30)
plt.title("Inventory Distribution")
plt.savefig("reports/inventory_distribution.png")
plt.show()

# Promotion Impact
plt.figure(figsize=(8,5))
sns.boxplot(
    x="Promotion_Flag",
    y="Sales_Quantity",
    data=df
)
plt.title("Promotion Impact on Sales")
plt.savefig("reports/promotion_impact.png")
plt.show()

# Correlation Heatmap
plt.figure(figsize=(10,6))

numeric_df = df.select_dtypes(include=["int64","float64"])

sns.heatmap(
    numeric_df.corr(),
    annot=False,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")
plt.savefig("reports/correlation_heatmap.png")
plt.show()