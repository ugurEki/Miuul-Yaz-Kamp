##### Küme (Set)
# - Değitirilebilir.
# - Sırasız + Eşsşizdir
# - Kapsayıcıdır.

# .difference() : iki kümenin farkı
# Veya set1 - set2 dediğindede aynı sonucu elde edersin.
set1 = set([1, 3, 5])
set2 = set([1, 2, 3])

print(set1.difference(set2))
print(set2.difference(set1))
print(set1 - set2)


# .symmetric_difference() : İki kümede de birbirlerine göre olmayanlar
print(set1.symmetric_difference(set2))

# .intersection() : İki kümenin kesişimi veya & sembolüde aynı anlama gelir.
set1 = set([1, 3, 5])
set2 = set([1, 2, 3])

print(set1.intersection(set2))
print(set1 & set2)

# .union() : iki kümenin birleşimi
print(set1.union(set2))
print(set2.union(set1))

# .isdisjoint() : İki kümenin kesişimi boş mu ?
set1 = set([7, 8, 9])
set2 = set([5, 6, 7, 8, 9, 10])

print(set1.isdisjoint(set2))

# .issubset() : Bir küme diğre kümenin alt kümesi mi ?
print(set1.issubset(set2))
print(set2.issubset(set1))

# .issuperset() : Bir küme diğer kümeyi kapsıyor mu ?
print(set2.issuperset(set1))
print(set1.issuperset(set2))



