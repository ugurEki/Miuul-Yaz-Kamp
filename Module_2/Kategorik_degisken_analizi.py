### Kategorik değişken analizi-1

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("titanic")

print(df.info())

cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]

num_but_cat = [col for col in df.columns if (df[col].nunique() < 10) and str(df[col].dtypes) in ["int64", "float64"]]

cat_but_cardinal = [col for col in df.columns if (df[col].nunique() > 20) and str(df[col].dtypes) in ["category", "object"]]

cat_cols_new = cat_cols + num_but_cat 

cat_cols_new = [col for col in cat_cols_new if col not in cat_but_cardinal]

def cat_summary(dataframe, col_name, plot = False):

    col_name_1 = dataframe[col_name].value_counts()
    ratio = 100 * dataframe[col_name].value_counts() / len(dataframe)
    print("{}: {}\nRatio: {}\n".format(col_name, col_name_1, ratio))
    print("###########################")
    if  dataframe[col_name].dtype == 'bool':
            dataframe[col_name] = dataframe[col_name].astype("int")
    if plot :
            sns.countplot(x = dataframe[col_name], data=dataframe)
            plt.show()
        

result = [cat_summary(df, col, plot = True) for col in cat_cols_new]

#print(cat_summary(df, "parch", plot=True))
print(result)
