# Enumerate : Otomatik Counter/Indexer ile for loop

students = ["John", "Mark", "Venesse", "Mariam"]

for index, student in enumerate(students):
    print(index, student)

# Tek indexdeki öğrencileri bir listeye, çift indexdeki öğrencileri başka listeye al.

def splitter(arg_list):
    odd = [] # tek
    even = [] # çift
    for index, arg in enumerate(arg_list):
        if index % 2 == 0:
            even.append(arg)
        else:
            odd.append(arg)
    return "tek liste: {}\nçift liste: {}".format(odd, even)



## Uygulama - Mülakat sorusu

# divide_students fonksiyonu yazınız.
# çift indexte yer alan öğrencileri bir listeye alınız.
# tek indexte yer alan öğrencileri bir listeye alınız.
# fakat bu iki liste tek bir liste olarak return olsun.

def divide_students(arg_list):
    odd = [] # tek
    even = [] # çift
    for index, arg in enumerate(arg_list):
        if index % 2 == 0:
            even.append(arg)
        else:
            odd.append(arg)

    join_liste = [odd] + [even]
    return join_liste

print(divide_students(students))

### Alternating fonksiyonun enumerate ile yazılması:

# before : "hi my name is john and i am learning python"
# after : "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"

string = "hi my name is john and i am learning python"

def text_converter(string):
    new_string = ""
    for index, character in enumerate(string):
        if index % 2 == 0:
            new_string += character.upper()
        else:
            new_string += character.lower()
    return new_string

print(text_converter(string))