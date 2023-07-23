import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#### Görev 1:

musteriler = pd.read_csv("Module_2\persona.csv")

print(musteriler.head())

print(musteriler.describe())

print(musteriler["PRICE"].nunique())

print(musteriler["PRICE"].value_counts())

print(musteriler.groupby("COUNTRY")["PRICE"].agg({"sum"}))

print(musteriler["SOURCE"].value_counts())

print(musteriler.groupby("COUNTRY")["PRICE"].agg({"mean"}))

print(musteriler.groupby("SOURCE")["PRICE"].agg({"mean"}))

print(musteriler.groupby(["COUNTRY", "SOURCE"])["PRICE"].agg({"mean"}))


#### Görev 2: 

print(musteriler.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"])["PRICE"].agg({"mean"}))

##### Görev 3: 

agg_df = musteriler.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"])["PRICE"].agg({"mean"}).sort_values(by = "mean", ascending = False)

##### Görev 4: 
agg_df = agg_df.reset_index()

print(agg_df.head())

##### Görev 5:
yas_araliklari = [0, 19, 24, 31, 41, 70]

etiketler = ['0_18', '19_23', '24_30', '31_40', '41_70']

agg_df["Age_cat"] = pd.cut(agg_df["AGE"], bins=yas_araliklari, labels=etiketler)

print(agg_df.head())

##### Görev 6:

cols = ["COUNTRY", "SOURCE", "SEX", "Age_cat"]

def concatenate_values(row):
    return f"{row['COUNTRY']}_{row['SOURCE']}_{row['SEX']}_{row['Age_cat']}"

# Create the new column using the apply function
agg_df['customers_level_based'] = agg_df.apply(concatenate_values, axis=1).str.upper()

print(agg_df.head())

## Yol 2: 

# iterrows() : Iterate over DataFrame rows as (index, Series) pairs.
agg_df['customers_level_based_2'] = [f"{row['COUNTRY']}_{row['SOURCE']}_{row['SEX']}_{row['Age_cat']}".upper() for _, row in agg_df.iterrows()]

print(agg_df.head())


#### Görev 7: 

agg_df["SEGMENT"] = pd.qcut(agg_df["mean"], 4, labels=["first", "second", "third","forth"])


print(agg_df.groupby("SEGMENT")["mean"].agg({"mean", "max", "sum"}))

#### Görev 8 :

first= agg_df[(agg_df["SOURCE"] == "android") & (agg_df["COUNTRY"] == "tur") & (agg_df["SEX"] == "female") & (agg_df["Age_cat"] == "31_40")]
second=agg_df[(agg_df["SOURCE"] == "ios") & (agg_df["COUNTRY"] == "fra") & (agg_df["SEX"] == "female") & (agg_df["Age_cat"] == "31_40")]
print(first)
print(second)





