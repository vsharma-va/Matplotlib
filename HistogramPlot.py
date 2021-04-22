import pandas as pd
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

data = pd.read_csv("Resources/data2.csv", sep=',')
df = pd.DataFrame(data)
responderID = df.Responder_id
age = df.Age

bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
plt.hist(age, bins=bins, edgecolor='k', log=True)
plt.tight_layout()
plt.show()

