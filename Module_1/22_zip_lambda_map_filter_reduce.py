## Zip : listeleri indexlerine göre match et ve birleştir

students = ["John", "Mark", "Venessa", "Mariam"]

departments = ["mathematics", "statistics", "physics", "astronomy"]

ages = [23, 30, 26, 22]

new_list = list(zip(students, departments, ages))

print(new_list)

## lambda : kullan at fonksiyonudur.

new_sum = lambda a, b : a + b # normalde bu kullanım yanlıştır sadece örnek olması açısından böyle yazdık.

print(new_sum(4, 5))

## map : ilgili fonksiyou değişkenler üzerinde uygulamamızı sağlar. 
# map(func, iter)

salaries = [1000, 2000, 3000, 4000, 5000]

def new_salary(x):
    return x * 20/100 + x

print(list(map(new_salary, salaries))) # for döngüsü yerine yazdık.

# şimdi new_salary fonksiyonu yerine lamda fonksiyonu ile map fonksiyonunu kullanarak tekrar yazalım:
# map(lambda, iterative)

print(list(map(lambda x: x * 20/100 + x, salaries)))

## Filter : filtreleme işlemleri için
list_store = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(filter(lambda x: x % 2 == 0, list_store)))


# map, filter, ve lambda beraber kullanımı.
print(list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, list_store))))


# Reduce :

from functools import reduce

list_store = [1, 2, 3, 4]
print(reduce(lambda a, b: a + b, list_store))

wages = [700, 800, 900, 1000]

print([wage * 1.1 if wage > 950 else wage * 1.2 for wage in wages])