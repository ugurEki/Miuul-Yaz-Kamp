## Görev 1: Verilen değerlerin veri yapılarını inceleyiniz.

x = 8
y = 3.2
z= 8j + 18
a = "Hello World"
b = True
c = 23 < 22
l = [1, 2, 3, 4]
d = {
    "Name": "Jake",
    "Age": 27,
    "Address": "Downtown"
}
t = ("Machine Learning", "Data Science")
s = {"Python", "Machine Learning", "Data Science"}

degiskenler = [x, y, z, a, b, c, l, d, t, s]

for d in degiskenler:
    print(type(d))

## Görev 2: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız.

text = "The goal is to turn data into information, and information into insight"

# yol 1:
liste = text.split()

new_list = [liste[index][:-1].upper() if "," in text else liste[index].upper() for (index, text) in enumerate(liste)]

print(new_list)

# yol 2:
for index, text in enumerate(liste):
    if text.endswith(","):
        liste[index] = liste[index].replace(",", "").upper()
    else:
        liste[index] = liste[index].upper()

print(liste)


## Görev 3: Verilen listeye aşağıdaki adımları uygulayınız

# Adım1: Verilen listenin elemansayısına bakınız.
# Adım2: Sıfırıncı ve onuncu indeksteki elemanları çağırınız.
# Adım3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.
# Adım4: Sekizinci indeksteki elemanı siliniz.
# Adım5: Yeni bir eleman ekleyiniz.
# Adım6: Sekizinci indekse "N" elemanını tekrar ekleyiniz.


lst = ["D", "A", "T", "A", "S", "C","I", "E","N", "C", "E",]

# adım 1:
print(len(lst))

# adım 2:
print(lst[0], lst[10])

# adım 3:
print(lst[0:4])

# adım 4:
lst.pop(8)
print(lst)

# adım 5:
lst.append("T")
print(lst)

# adım 6: 
lst.insert(8, "N")
print(lst)

## Görev 4: Verilen sözlük yapısına aşağıdaki adımları uygulayınız.

# Adım1: Key değerlerine erişiniz.
# Adım2: Value'lara erişiniz.
# Adım3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
# Adım4: Key değeri Ahmet value değeri[Turkey,24] olan yeni bir değer ekleyiniz.
# Adım5: Antonio'yu dictionary'den siliniz.

dict = {
    "Christian": ["America", 18],
    "Daisy": ["England", 12],
    "Antonio": ["Spain", 22],
    "Dante": ["Italy", 25]
}

# Adım 1:
print(dict.keys())

# Adım 2:
print(dict.values())

# Adım 3:
dict["Daisy"][1] = 13
print(dict)

# Adım 4:
dict["Ahmet"] = ["Turkey", 24]
print(dict)

# Adım 5:
dict.pop("Antonio")
print(dict)

## Görev 5: Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve
# bu listeleri return eden fonksiyon yazınız.

lis = [2, 13, 18, 93, 22]
def func(data = []):
    odd = []
    even = []
    for l in data:
        if l % 2 == 0:
            even.append(l)
        else:
            odd.append(l)
    return odd, even

print(func(lis))

## Görev 6:

ogrenciler = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]

for index, student in enumerate(ogrenciler):
    if index < 3:
        print("Mühendislik Fakültesi {} . öğrenci: {}".format(index, student))
    else:
        print("Tıp Fakültesi {} . öğrenci: {}".format(index, student))

## Görev 7:
ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]

kredi = [3, 4, 2, 4]

kontenjan = [30, 75, 150, 25]

new = list(zip(kredi, ders_kodu, kontenjan))

for i in new:
    print("Kredisi {} olan {} kodlu dersin kontenjanı {} kişidir.".format(i[0], i[1], i[2]))

## Görev 8:
kume1 = set(["data", "python"])
kume2 = set(["data", "funtion", "qcut", "lambda", "python", "miuul"])

if kume1.issuperset(kume2):
    print(kume1.intersection(kume2))
else:
    print(kume2.difference(kume1))


