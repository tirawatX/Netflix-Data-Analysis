import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("data/netflix_titles.csv")

# Missing Values Analysis

print("\n========== MISSING VALUES ==========")

missing = df.isnull().sum()

print(missing)

# Calculate Missing Percentage
missing_percent = (df.isnull().sum() / len(df)) * 100

print("\n========== MISSING PERCENTAGE ==========")

print(missing_percent.sort_values(ascending=False).round(2))

print("\n========== DUPLICATE DATA ==========")

print("Duplicate Rows:", df.duplicated().sum())

print("\n========== CONTENT TYPES ==========")

print(df["type"].value_counts())

print("\n========== RATINGS ==========")

print(df["rating"].value_counts())

print("\n========== RELEASE YEARS ==========")

print(df["release_year"].value_counts().head(10))