import pandas as pd


df = pd.read_csv("data/processed/netflix_cleaned.csv")

print(df["type"].value_counts())