# Sözlük (Dictionary)
# - Değiştirilebilir.
# - Sırasız. (3.7 sonra sıralı)
# - Kapsayıcı.

dictionary = {"REG": "Regression",
              "LOG": "Logistic Regression", 
              "CART": "Classification and Reg"}
print(dictionary)

print(dictionary["REG"])

dic_2 = {"REG": ["RMSE", 10],
         "LOG": ["MSE", 20],
         "CART": ["SSE", 30]}

print(dic_2)
print(dic_2["CART"][1])

# Key sorgulama
print("REG" in dic_2)

# Key'e göre Value'ya erişmek
print(dic_2.get("REG"))

# Value dğiştirmek
dic_2["REG"] = ["YSA", 10]
print(dic_2)

# Tüm Key'lere ve Value'lere erişmek
print(dic_2.keys())
print(dic_2.values())

# Tüm çiftleri Tuple halinde listeye çevirme.
print(dic_2.items())

# yeni değer atamak veya yeni key-value çifti eklemek.
dic_2.update({"REG": 11})
print(dic_2)

dic_2.update({"RF": 10})
print(dic_2)
