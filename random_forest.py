import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv(
    "dataset/feature_engineered_fmcg.csv"
)

# Encode Target
mapping = {
    "Low":0,
    "Medium":1,
    "High":2
}

df["Demand_Category"] = df["Demand_Category"].map(mapping)

X = df[
[
"Inventory_Level",
"Price",
"Promotion_Flag"
]
]

y = df["Demand_Category"]

X_train, X_test, y_train, y_test = train_test_split(
    X,y,test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train,y_train)

pred = model.predict(X_test)

print(
    "Accuracy:",
    accuracy_score(y_test,pred)
)