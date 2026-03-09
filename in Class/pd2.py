import pandas as pd
import os

dir = os.path.dirname(os.path.abspath(__file__))
# Reading — returns a DataFrame
df = pd.read_csv(os.path.join(dir, 'students.csv'))

print(df)
#       name  score grade
# 0    Alice     92     A
# 1      Bob     78     B
# 2  Charlie     65     C

print(df.shape)           # (3, 3) — rows, columns
print(df.columns.tolist()) # ['name', 'score', 'grade']
print(df['score'].mean())  # 78.33 — pandas infers numeric types automatically

# Access a column
print(df['name'])          # Series: Alice, Bob, Charlie

# Access a single value
print(df.loc[0, 'name'])   # 'Alice'

# Filter rows
passing = df[df['score'] >= 70]

# Writing back to CSV
df.to_csv('output.csv', index=False)  # index=False removes the row numbers