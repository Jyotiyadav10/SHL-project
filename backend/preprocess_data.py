# preprocess_data.py
import pandas as pd

df = pd.read_csv("catalog.csv")

# Remove duplicates
df = df.drop_duplicates(subset=["url"])

# Fill missing values if any
df['category'] = df['category'].fillna("Unknown")
df['test_type'] = df['test_type'].fillna("K")

df.to_csv("catalog.csv", index=False)
print("catalog.csv cleaned and saved.")
