# Fonksiyon içerisinden fonksiyon çağırmak 

def calculate(varm, moisture, charge):
    return int((varm + moisture) / charge)

calculate(90, 12, 12) * 10

def standardization(a, p):
    return a * 10 / 100 * p * p

print(standardization(45, 1))

def all_calculation(varm, moisture, charge, p):
    a = calculate(varm, moisture, charge)
    b = standardization(a, p)
    return b * 10

print(all_calculation(1, 3, 5, 12))