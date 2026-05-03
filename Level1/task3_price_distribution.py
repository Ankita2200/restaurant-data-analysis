import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Dataset .csv")

sns.countplot(x='Price range', data=df)
plt.title("Price Distribution")
plt.savefig("Output/price.png")
plt.show()