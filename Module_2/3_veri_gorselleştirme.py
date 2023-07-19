### Kategorik ve görselleştirme : bar plot, pie chart

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = sns.load_dataset("titanic", None)

# print(df.head())

#df["sex"].value_counts().plot(kind = "bar")
#plt.show()

### Sayısal değişken görselleştirme : histogram ve boxplot

#plt.hist(df["age"])

#plt.show()

#plt.boxplot(df["fare"])

#plt.show()

### Matplotlib some features:

x = np.array([1, 8])
y = np.array([0, 150])

#plt.plot(x, y, 'o')
#plt.show()

x = np.array([2, 4, 6, 8, 10])
y = x ** 3

#plt.plot(y, linestyle = 'dashdot', color = 'r')
#plt.show()


### Seaborn some features

df = sns.load_dataset("tips")

print(df.head())

#sns.countplot(x = df["sex"], data = df)

#plt.show()


#sns.boxplot(df["total_bill"])
sns.scatterplot(x = df["tip"], y = df["total_bill"], hue=df["smoker"])
plt.show()