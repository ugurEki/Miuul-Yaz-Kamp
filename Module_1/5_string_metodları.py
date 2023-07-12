# String(Karakter Dizisi) metodları 

print(dir(str)) # Stringe ait fonksiyonlar hakkında bilgi sahibi olmak için

name = "John"
print(type(name))
print(type(len))
print(len(name))
print(len("Miuul Makine Öğrenmesi Yaz Kampı"))
print(len("MiuulMakineÖğrenmesiYazKampı")) # Boşluklarda karakter olarak sayılır

# .upper() & .lower() : küçük-büyük dönüşümleri
print("miuul".upper())
print("UĞUR".lower())

# .replace() : karakter değiştir
hi = "Hello AI Era"
print(hi.replace("l", "p"))

# .split() : böler
print(hi.split())

# .strip() : kırpar
txt = " ofofo "
print(txt.strip("o"))
print(txt.strip())

# .capitalize()
txt = "foo"
print(txt.capitalize())

# .startswith()
txt = "uğur"
print(txt.startswith("u"))




