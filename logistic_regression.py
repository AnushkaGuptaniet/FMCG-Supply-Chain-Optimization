import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

# Load Dataset
df = pd.read_csv(
    "dataset/feature_engineered_fmcg.csv"
)

# Encode Target Variable
le = LabelEncoder()

df["Demand_Category"] = le.fit_transform(
    df["Demand_Category"]
)

# Features
X = df[
[
"Inventory_Level",
"Price",
"Promotion_Flag"
]

]

# Target
y = df["Demand_Category"]

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = LogisticRegression(
    max_iter=1000
)

model.fit(
    X_train,
    y_train
)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
print("\nAccuracy Score:")
print(
    accuracy_score(y_test, y_pred)
)

# Confusion Matrix
print("\nConfusion Matrix:")
print(
    confusion_matrix(
        y_test,
        y_pred
    )
)

# Classification Report
print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred
    )
)