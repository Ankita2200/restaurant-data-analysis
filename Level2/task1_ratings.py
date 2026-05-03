import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Dataset .csv")

sns.histplot(df['Aggregate rating'], bins=10)
plt.title("Ratings")
plt.savefig("Output/rating.png")
plt.show()