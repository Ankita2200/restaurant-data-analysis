import pandas as pd

df = pd.read_csv("Dataset .csv")

service = df.groupby('Price range')[['Has Online delivery','Has Table booking']].apply(lambda x: (x=='Yes').mean())
print(service)