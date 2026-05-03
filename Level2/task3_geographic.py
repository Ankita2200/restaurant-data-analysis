import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Dataset .csv")

plt.scatter(df['Longitude'], df['Latitude'])
plt.title("Map")
plt.savefig("Output/map.png")
plt.show()