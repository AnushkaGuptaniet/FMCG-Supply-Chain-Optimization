# import pandas as pd

# df = pd.read_csv("dataset/FMCG_Full_Requirement_Dataset.csv")

# # Remove duplicates
# df.drop_duplicates(inplace=True)

# # Convert Date column
# df["Date"] = pd.to_datetime(df["Date"])

# # Fill missing numeric values
# numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns

# for col in numeric_cols:
#     df[col] = df[col].fillna(df[col].mean())

# # Fill missing categorical values
# categorical_cols = df.select_dtypes(include=["object"]).columns

# for col in categorical_cols:
#     df[col] = df[col].fillna(df[col].mode()[0])

# print("Cleaning Completed")
# print(df.isnull().sum())

# df.to_csv("dataset/clean_fmcg.csv", index=False)

# print("Clean dataset saved successfully!")

# import pandas as pd

# df = pd.read_csv("dataset/FMCG_Full_Requirement_Dataset.csv")

# print(df.info())

import pandas as pd

# Load dataset
df = pd.read_csv("dataset/FMCG_Full_Requirement_Dataset.csv")

print("Original Shape:", df.shape)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# Fill missing numerical values
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns

for col in numeric_cols:
    df[col] = df[col].fillna(df[col].mean())

# Fill missing categorical values
categorical_cols = df.select_dtypes(include=["object"]).columns

for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Save cleaned dataset
df.to_csv("dataset/clean_fmcg.csv", index=False)

print("\nClean dataset saved successfully!")