import pandas as pd

df = pd.read_csv("Dataset .csv")

print(df['Has Online delivery'].value_counts(normalize=True)*100)

print(df.groupby('Has Online delivery')['Aggregate rating'].mean())