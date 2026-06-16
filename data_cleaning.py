
# import pandas as pd

# df = pd.read_csv("dataset/FMCG_Full_Requirement_Dataset.csv")

# print(df.info())

import pandas as pd

df = pd.read_csv("dataset/FMCG_Full_Requirement_Dataset.csv")

print(df.info())
print("\nMissing Values:")
print(df.isnull().sum())