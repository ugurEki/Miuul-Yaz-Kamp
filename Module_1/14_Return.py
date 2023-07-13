# Return : Fonksiyon çıktılarını girdi olarak kullanmak.

def calculate(varm, moisture, charge):
    # print(varm + moisture)/charge)
    return (varm + moisture)/charge


# eğer return değilde print kullansayıdık hata vericekti.
# print dediğimizde nonetype olur ve nonetype'ı interger bir değer ile çarpamazsın.
# return burada bize çıktıyı bir girdi gibi kullanmamızı sağlar.

calculate(98, 12, 78) * 10

def calculate(varm, moisture, charge):
    varm = varm * 2
    moisture = moisture * 2
    charge = charge * 2
    output = (varm + moisture) / charge

    return varm, moisture, charge, output

print(type(calculate(98, 12, 78))) # tuple 

varm, moisture, charge, output = calculate(98, 12, 78)

print(varm, moisture, charge, output, sep="\n")