import pandas as pd

df = pd.read_csv("Dataset .csv")

print("City with most restaurants:", df['City'].value_counts().idxmax())

avg = df.groupby('City')['Aggregate rating'].mean()
print("City with highest rating:", avg.idxmax())