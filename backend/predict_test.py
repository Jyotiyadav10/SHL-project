# predict_test.py
import pandas as pd
from recommend import recommend_assessments

# Example SHL test queries
test_queries = [
     "I am hiring for Java developers who can also collaborate effectively with my business teams.",
    "Looking to hire mid-level professionals who are proficient in Python, SQL and Java Script.",
    "Here is a JD text, can you recommend some assessment that can help me screen applications. I am hiring for an analyst and wants applications to screen using Cognitive and personality tests",
    "Need a manager skilled in project coordination and leadership.",
    "Hiring HR personnel with strong communication skills.",
    "Hiring a data scientist with Python and machine learning knowledge.",
    "Looking for a finance professional with accounting and auditing skills.",
    "Hiring a marketing analyst with creativity and analytical skills.",
    "Need a software tester proficient in automation and manual testing."
]

rows = []
for q in test_queries:
    recs = recommend_assessments(q, top_k=10)
    row = {"Query": q}
    for i, r in enumerate(recs, start=1):
        row[f"Recommendation {i}"] = r['url']
    rows.append(row)

df = pd.DataFrame(rows)
df.to_csv("submission.csv", index=False)
print("submission.csv saved successfully.")
