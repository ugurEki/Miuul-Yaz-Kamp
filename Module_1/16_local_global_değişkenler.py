# Lokal & Global değişkenler

list_store = [1, 2] # global bir değişkendir.

def add_element(a, b):
    c = a * b # Lokal değişken
    # c değişkeni list_store'a ekle.
    list_store.append(c)
    print(list_store)
