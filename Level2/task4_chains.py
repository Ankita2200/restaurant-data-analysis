import pandas as pd

df = pd.read_csv("Dataset .csv")

chains = df['Address'].value_counts()
print(chains[chains > 1].head())