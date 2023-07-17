### Pandas Series

import pandas as pd

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

df.drop("age", axis = 1, inplace = True).head() # kalıcı : inplace = True

df.reset_index().head()

df = df.reset_index()

df.head()





