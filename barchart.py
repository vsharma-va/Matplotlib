from matplotlib import pyplot as plt
import csv
import pandas as pd
from collections import Counter

plt.style.use("fivethirtyeight")

# using csv reader
with open('Resources/data1.csv') as csvFile:
    csvReader = csv.DictReader(csvFile)

    row = next(csvReader)
    listLanguages = row['LanguagesWorkedWith'].split(';')
    totalRepetition = Counter(listLanguages)
    skipLine = 0

    for row in csvReader:
        if skipLine >= 1:
            listLanguages = row['LanguagesWorkedWith'].split(';')
            totalRepetition.update(listLanguages)
        skipLine += 1

languageFrequency = list(totalRepetition.values())
languageName = list(totalRepetition.keys())

plt.title("Languages Popularity")
plt.xlabel('Language Name')
plt.ylabel('Number Of People')
plt.barh(languageName, languageFrequency, label='Popularity')
plt.legend('upper right')
plt.tight_layout()
plt.show()

# Using pandas
data = pd.read_csv("Resources/data1.csv", sep=',')
df = pd.DataFrame(data)

requiredColumn = df.LanguagesWorkedWith
plottingData = Counter()

for languages in requiredColumn:
    lang = (languages.split(';'))
    plottingData.update(lang)

popularity = list(plottingData.values())
langNames = list(plottingData.keys())

plt.xlabel("Language Names")
plt.ylabel("Popularity")
plt.barh(langNames, popularity)
plt.tight_layout()
plt.show()
