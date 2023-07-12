# Liste (list)
# - Değiştirilebilir.
# - Listeler Sıralıdır. Index işlemcileri yapılabilir.
# - Kapsayıcıdır.

notes = [1, 2, 3, 4]
print(type(notes))

names = ["a", "b", "v", "d"]
print(names)

not_nam = [1, 2, 3, "a", "b", True, [1, 2, 3]]
print(not_nam)

print(not_nam[0])
print(not_nam[5])
print(not_nam[6])
print(not_nam[6][1])

notes[0] = 90
print(notes)

print(not_nam[0:4])

###### Liste Metodları

# .append() : eleman ekler
notes.append(["Bir", "İki", "Üç"])
print(notes)

# .pop() : indexe göre siler
notes.pop(0) # 1 sayısını siler.
print(notes)

# .insert() : indexe ekler
notes.insert(2, 3.5)
print(notes)




