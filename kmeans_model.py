# import pandas as pd

# from sklearn.cluster import KMeans
# from sklearn.preprocessing import LabelEncoder
# from sklearn.preprocessing import StandardScaler

# # Load dataset
# df = pd.read_csv(
#     "dataset/feature_engineered_fmcg.csv"
# )

# # Select Features
# features = [
#     "Inventory_Level",
#     "Sales_Quantity",
#     "Price",
#     "Promotion_Flag"
# ]

# X = df[features]

# # Scale Data
# scaler = StandardScaler()

# X_scaled = scaler.fit_transform(X)

# # K-Means
# kmeans = KMeans(
#     n_clusters=3,
#     random_state=42,
#     n_init=10
# )

# df["Cluster"] = kmeans.fit_predict(
#     X_scaled
# )

# # Cluster Summary
# print(
#     df.groupby("Cluster")[features].mean()
# )

# # Save Dataset
# df.to_csv(
#     "dataset/kmeans_output.csv",
#     index=False
# )

# print("\nK-Means Completed Successfully")

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv(
    "dataset/feature_engineered_fmcg.csv"
)

X = df[
[
"Inventory_Level",
"Sales_Quantity"
]
]

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

df["Cluster"] = kmeans.fit_predict(
    X_scaled
)

plt.figure(figsize=(8,6))

plt.scatter(
    df["Inventory_Level"],
    df["Sales_Quantity"],
    c=df["Cluster"]
)

plt.xlabel("Inventory Level")
plt.ylabel("Sales Quantity")
plt.title("K-Means Clustering")

plt.show()