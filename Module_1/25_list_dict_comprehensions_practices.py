### List & Dict Comprehension uygulamalar

# Bir veri setindeki değişken isimlerini değiştirmek

# Before :
# ["total", "speeding", "alcohol", "not_distracted", "no_previous", "ins_premium", "ins_losses", "abbrev"]

# after :
# ["TOTAL", "SPEEDING", "ALCOHOL", "NOT_DISTRACTED", "NO_PREVIOUS", "INS_PREMIUM" .....]


import seaborn as sns

df = sns.load_dataset("car_crashes")
print(df.columns)

df.columns = [column.upper() for column in df.columns]

print(df.columns)

## İsminde "INS" olan değişkenlerin başına FLAG diğerlerine NO_FLAG eklemek istiyoruz.

df.columns = ["FLAG_" + column if "INS" in column else "NO_FLAG_" + column for column in df.columns]

print(df.columns)


# Yeni Amaç : Amaç key'i string, value'su aşağıdaki gibi bir liste olan sözlük oluşturmak.

# ["mean", "min", "max", "var"]

# {"total" : ["mean", "min", "max", "var"], 
#  "speeding" : ["mean", "min", "max", "var"], 
#  "alcohol" : ["mean", "min", "max", "var"], 
#  "not_distracted" : ["mean", "min", "max", "var"], 
#  "no_previous" : ["mean", "min", "max", "var"], 
#  "ins_premium" : ["mean", "min", "max", "var"], 
#  "ins_losses" : ["mean", "min", "max", "var"], 
#  "abbrev" : ["mean", "min", "max", "var"]}

df_2 = sns.load_dataset("car_crashes")

new_dict = {column: ["mean", "min", "max", "var"] for column in df_2.columns if df_2[column].dtype != "O"}

print(df_2[new_dict.keys()].aggregate(new_dict))

