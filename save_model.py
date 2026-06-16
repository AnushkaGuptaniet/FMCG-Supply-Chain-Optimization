import os
import pickle
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Create models folder if not exists
os.makedirs("models", exist_ok=True)

# Load dataset
df = pd.read_csv("dataset/feature_engineered_fmcg.csv")

# Convert target labels to numbers
mapping = {
    "Low": 0,
    "Medium": 1,
    "High": 2
}

df["Demand_Category"] = df["Demand_Category"].map(mapping)

# Features
X = df[[
    "Inventory_Level",
    "Price",
    "Promotion_Flag"
]]

# Target
y = df["Demand_Category"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

# Save model
with open("models/demand_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model Saved Successfully!")