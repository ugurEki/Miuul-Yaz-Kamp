### Pandas Series

import pandas as pd
import numpy as np

ser = pd.Series([10, 77, 12, 4, 5])

print(ser)
print(type(ser))
print(ser.index)
print(ser.dtype)
print(ser.size)
print(ser.ndim)
print(ser.values)
print(ser.head())
print(ser.tail())

### Veri Okuma

customer = pd.read_csv(r"C:\Users\HP\Downloads\AdventureWorks+CSV+Files\AdventureWorks_Customers.csv", encoding='latin1')

# print(customer.head(5))

### Veriye hızlı bakış

import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")

print(df.head())
print(df.tail())
print(df.info())
print(df.shape)
print(df.columns)
print(df.index)
print(df.describe().T)
print(df.isnull().values.any()) # En az bir tane dahi olsa null değer var mı ?
print(df.isnull().sum())
print(df["sex"].value_counts())

print(df[0:13])

df.drop(0, axis=0) # axis = 0(satır sil)

df.index = df["age"]

df.drop("age", axis = 1, inplace = True) # kalıcı : inplace = True

df.reset_index().head()

df = df.reset_index()

df.head()

### loc & iloc

df = sns.load_dataset("titanic")

df.iloc[0:3, 0]

df.loc[0:3, ["age", "sex", "embarked", "alive"]]

### Koşullu seçim işlemleri

df[df["age"] > 50]["age"].count()

df.loc[df["age"] > 50, ["age", "class"]].head()

df.loc[(df["age"] > 50) 
       & (df["sex"] == "male") 
       & ((df["embarked"] == "Cherbourg") | (df["embarked"] == "Southampton")), 
       ["age", "class", "embarked"]].head()

### Toplulaştırma ve Gruplama (Aggregation & Grouping)

df.groupby("sex")["age"].mean()

df.groupby(["sex", "embark_town", "class"]).agg({
    "age": ["mean", "sum"],
    "survived": "mean",
    "sex": "count"})

### pivot table

df["new_age"] = pd.cut(df["age"], [0, 10, 18, 25, 40, 90])

print(df.head(8))

print(df.pivot_table(values = "survived",
                     index = "sex",
                     columns = ["new_age"]))


### Apply ve lambda

df["age2"] = df["age"] * 2
df["age3"] = df["age"] * 5


df[["age", "age2", "age3"]].apply(lambda x: x / 10).head()

df.loc[:, df.columns.str.contains("age")].apply(lambda x: (x - x.mean()) / x.std()).head() # normalize age columns

### Birleştirme (Join) işlemleri

m = np.random.randint(1, 30, size=(5, 3))
df1 = pd.DataFrame(m, columns=["var1", "var2", "var3"])
df2 = df1 + 99

pd.concat([df1, df2], ignore_index=True) # alt alta birleştirmek. 

## Merge

df1 = pd.DataFrame({
    "employees": ["john", "dennis", "mark", "maria"],
    "group": ["accounting", "engineering", "engineering", "hr"]
})

df2 = pd.DataFrame({
    "employees": ["mark", "john", "dennis", "maria"],
    "start_date": [2010, 2009, 2014, 2019]
})

pd.merge(df1, df2, on = "employees")







