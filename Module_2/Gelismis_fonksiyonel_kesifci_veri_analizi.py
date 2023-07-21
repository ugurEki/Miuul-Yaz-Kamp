### Gelişmiş Fonksiyonel Keşifçi Veri Analizi (Advanced Functional EDA)

# - Genel Resim.
# - Kategorik değişken analizi. (Analysis of categorical variables)
# - Sayısal değişkenlerin analizi. (Analysis of numerical variables)
# - Hedef değişkenlerin analizi. (Analysis of target variables)
# - Korelasyon analizi. (Analysis of Correlation)

## 1. Genel Resim

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("titanic")

def check_df(dataframe, head = 5):
    print("############### Shape ###############")
    print(dataframe.shape)
    print("############### Types ###############")
    print(dataframe.dtypes)
    print("############### Head ###############")
    print(dataframe.head(head))
    print("############### Tail ###############")
    print(dataframe.tail(head))
    print("############### NA ###############")
    print(dataframe.isnull().sum())
    print("############### Quantiles ###############")
    print(dataframe.describe([0, 0.05, 0.5, 0.95, 0.99, 1]).T)


print(check_df(df))


