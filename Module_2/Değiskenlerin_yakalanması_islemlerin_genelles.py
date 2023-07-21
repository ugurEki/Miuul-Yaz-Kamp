## capturing variables and generalizing operations.

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("titanic")

print(df.info())


def types_list(dataframe):
    """
    This function takes an input as a dataframe and split 
    up the columns of dataframe into two categories. 
    These categories are cat_variables which are categorical variables 
    and quant_variables are which quantitative or numerical variables.

    Args :
        dataframe : pandas dataframe 
    
    Return:
        cat_variables: categorical variables.
        quant_variables : quantitative variables.

    example:
        df = pd.read_csv("example.csv")
        cat_variables, quant_variables = types_list(df)
        print(quant_variables)
        >> [75, 86, 92, 12]

    """
    quant_types = ["int64", "float64"]
    cat_types = ["object", "category", "bool"]

    cat_variables = []
    quant_variables = []
    for col in dataframe.columns:
        if (dataframe[col].dtype in quant_types) and (dataframe[col].nunique() > 10):
            quant_variables.append(col)
        else:
            cat_variables.append(col)
    return cat_variables, quant_variables

categorical_variables, quantitative_variables = types_list(df)

def quant_summary(dataframe, col_name):
    
    print("############### Descriptive Statistics ###############")
    print(dataframe[col_name].describe().T)
    sns.boxplot(x = dataframe[col_name])
    plt.show()
    sns.histplot(dataframe[col_name])
    plt.show()

for var in quantitative_variables:
    quant_summary(df, var)


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


for cat_var in categorical_variables:
    cat_summary(df, cat_var, plot=True)

