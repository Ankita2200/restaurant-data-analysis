import pandas as pd

df = pd.read_csv("Dataset .csv")

cuisine_series = df['Cuisines'].str.split(', ').explode()
top = cuisine_series.value_counts().head(3)

print(top)