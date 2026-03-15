import pandas as pd

df = pd.read_csv("../data/cleaned_jobs.csv")

print("Total Jobs:", len(df))

print("\nTop 10 Job Titles:")
print(df["job_title"].value_counts().head(10))

print("\nAverage Salary by Experience Level:")
print(df.groupby("experience_level")["salary_in_usd"].mean())

print("\nTop 10 Highest Paying Jobs:")
print(df.groupby("job_title")["salary_in_usd"].mean().sort_values(ascending=False).head(10))