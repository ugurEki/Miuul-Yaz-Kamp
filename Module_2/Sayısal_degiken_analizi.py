import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("titanic")

print(df.head())

print(df.info())

# Sayısal categoriler : int64, float64

quantitative_variables = [col for col in df.columns if (df[col].dtype in ["int64", "float64"]) and (df[col].nunique() > 10)]


# descriptive statistics.
# histogram and box plot.
def quant_summary(dataframe, col_name):
    
    print("############### Descriptive Statistics ###############")
    print(dataframe[col_name].describe().T)
    sns.boxplot(x = dataframe[col_name])
    plt.show()
    sns.histplot(dataframe[col_name])
    plt.show()

for var in quantitative_variables:
    quant_summary(df, var)



