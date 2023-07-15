# Dict comprehension

dictionary = {"a": 1,
              "b": 2,
              "c": 3,
              "d": 4}

d1 = {key: value ** 2 for (key, value) in dictionary.items()}

print(d1)

d2 = {key.upper(): value for (key, value) in dictionary.items()}

print(d2)

d3 = {key.upper(): value ** 2 for (key, value) in dictionary.items()}

print(d3)

### Uygulama : Dict comprehensions mülakat sorusu
# Amaç : çift sayıların karesi alınarak bir sözlüğe eklenmek istenmektedir.

# eski klasik yöntem

numbers = range(10)
new_dict = {}

for number in numbers:
    if number % 2 == 0:
        new_dict[number] = number ** 2

print(new_dict)

# dict comprehensions

new_dict = {number: number ** 2  for number in numbers if number % 2 == 0}

print(new_dict)
