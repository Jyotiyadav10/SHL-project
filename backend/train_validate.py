import pandas as pd
from recommend import recommend

# Load labeled dataset
train_df = pd.read_excel("Gen_AI_Dataset.xlsx", sheet_name="catalog")

for idx, row in train_df.iterrows():
    query = row['Query']
    recommended = recommend(query, top_k=5)
    print(f"\nQuery: {query}")
    print(recommended)
