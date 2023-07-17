import numpy as np

# numpy ın faydasını göstermek açısından 
# numpy kullanmadan ve kullanarak örnek bir kod yazıcam.
a = [1, 2, 3, 4]
b = [2, 3, 4, 5]

ab = []

for i in range(0, len(a)):
    ab.append(a[i] * b[i])

print(ab)

# numpy yolu
a_1 = np.array([1, 2, 3, 4])
b_1 = np.array([2, 3, 4, 5])

print(a_1 * b_1)

print(type(a_1))

# sıfırlardan oluşan ve integer data type sahip numpy array.
zeros = np.zeros(10, dtype = int)
print(zeros)

# 0 ile 10 arasında rastgele 10 tane integer değerden oluşan bir array.
random = np.random.randint(0, 10, 10)

print(random)

# ortalaması 10 olan, standart sapması 4 olan ve (3, 4)(3 satır ve 4 sütundan oluşan - 2D array)
# boyutunda olan rastgele bir normal dağılım arrayi oluştur.
normal = np.random.normal(loc=10, scale=4, size=(3, 4))
print(normal)

### NumPy array özellikleri :

# - ndim : boyut sayısı
# - shape : boyut bilgisi.
# - size : toplam eleman sayısı.
# - dtype : array veri tipi

a = np.random.randint(0, 10, size=5)

print(a)

print(a.ndim)
print(a.shape)
print(a.size)
print(a.dtype)


### Reshaping (Yeniden şekillendirme)

b = np.random.randint(1, 10, size=9)
print(b)

# (3, 3) 3 satır ve 3 sütundan oluşan.
new_b = b.reshape(3, 3)
print(new_b)

### Index Seçimi (Index Selection)

a = np.random.randint(0, 10, size=10)

print(a[0]) # 0'ıncı index.
print(a[0:5]) # 0 dan 5 inci indexe kadar(5 hariç) bastır.

a[0] = 999 # belirli bir indexteki  değeri değiştirme.

# 3 satır ve 5 sütundan oluşan 2d array
m = np.random.randint(0, 10, size=(3, 5))

print(m[0, 0]) # satır - sütun bilgisi verilmeli (2 boyutlu)
print(m[2, 3]) # 2. satır ve 3. sütun
print(m[:, 0]) # bütun satırlardaki 0'ıncı sütunu seç.
print(m[1, :]) # 1. inci satır ve büyün sütunlar.
print(m[0:2, 0:3]) # 0 ve 1. inci satır | 0 dan 3.indexe kadar. al.


### Fancy index :

v = np.arange(0, 30, 3)

catch = [1, 2, 3]
# catch deki sayılara gelen indexteki değerleri döndürür.
print(v[catch])

### NumPy'da koşullu işlemler

v = np.array([1, 2, 3, 4, 5])

print(v[v < 3])

### Matematiksel işlemler.

v = np.array([1, 2, 3, 4, 5])

# bütün elemanları 5 e böl.
print(v / 5)

# bütün elemanlar - karesini al
print(v**2)

# matematiksel işlemler için bazı numpy metodları
print(np.subtract(v, 1))
print(np.add(v, 1))
print(np.mean(v))
print(np.sum(v))
print(np.min(v))
print(np.max(v))
print(np.var(v))