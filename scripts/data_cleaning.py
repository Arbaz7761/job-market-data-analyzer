import pandas as pd

df = pd.read_csv("../data/ds_salaries.csv")

print(df.head())

print(df.columns)

df = df.drop_duplicates()

print("Rows after removing duplicates:", df.shape)

print(df.isnull().sum())

df = df.drop(columns=["Unnamed: 0"])

df.to_csv("../data/cleaned_jobs.csv", index=False)

print("Cleaned dataset saved successfully")