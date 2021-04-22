import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

data = pd.read_csv("Resources/data.csv")
df = pd.DataFrame(data)

age = df.Age
devSalaries = df.All_Devs
pySalaries = df.Python
javaSalaries = df.JavaScript
overallMedian = 57287

plt.plot(age, devSalaries, color='b', linestyle='--', label='All Devs')

plt.plot(age, pySalaries, color='k', label='Python Devs')
plt.fill_between(age, pySalaries, devSalaries, where=(pySalaries >= devSalaries), interpolate=True, alpha=0.25,
                 label='Above Average')
plt.fill_between(age, pySalaries, devSalaries, where=(pySalaries <= devSalaries), interpolate=True, color='red',
                 alpha=0.25, label='Below Average')

plt.legend()
plt.title("Median Salary (USD) by age")
plt.xlabel("Age")
plt.ylabel("Median Salary (USD)")

plt.show()
