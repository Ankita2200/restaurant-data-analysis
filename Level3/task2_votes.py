import pandas as pd

df = pd.read_csv("Dataset .csv")

print(df.nlargest(3,'Votes')[['City','Votes']])
print(df[['Votes','Aggregate rating']].corr())