import pandas as pd

df = pd.DataFrame({
    'name':  ['Alice', 'Bob', 'Charlie'],
    'score': [92, 78, 65],
    'grade': ['A', 'B', 'C']
})

print(df)

#       name  score grade
# 0    Alice     92     A
# 1      Bob     78     B
# 2  Charlie     65     C