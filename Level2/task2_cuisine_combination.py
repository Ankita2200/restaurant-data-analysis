import pandas as pd

df = pd.read_csv("Dataset .csv")

print(df['Cuisines'].value_counts().head())