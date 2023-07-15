## Görev 1:
import seaborn as sns

df = sns.load_dataset("car_crashes")

df.columns = ["NUM_" + column.upper() if df[column].dtype != "O" else column.upper() for column in df.columns]

print(df.columns)

## Görev 2:

df_2 = sns.load_dataset("car_crashes")

df_2.columns = [column.upper() + "_FLAG" if "no" not in column else column.upper() for column in df_2.columns]

print(df_2.columns)

## Görev 3:
df_3 = sns.load_dataset("car_crashes")

og_list = ["abbrev", "no_previous"]

new_cols = [column for column in df_3.columns if column not in og_list]

new_df = df_3[new_cols]

print(new_df.head())