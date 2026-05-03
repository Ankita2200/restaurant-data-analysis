import pandas as pd

df = pd.read_csv("Dataset .csv")

df['Review Length'] = df['Rating text'].astype(str).apply(len)

print(df['Review Length'].mean())
print(df[['Review Length','Aggregate rating']].corr())