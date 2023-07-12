# Karakter dizileri ( Strings )
print("John")
print('John')

name = "John"
print(name)

# Çok satırlı karakter dizileri
text = """Publishing Packages: 
If you have developed a Python package and want to share it with others,
you can publish it to PyPI. You will need to create a PyPI account
and follow the publishing guidelines, which typically involve
creating a setup.py file with package metadata and using the twine tool
to upload your package."""

print(text)

# Karakter dizilerinin elemanlarına erişmek
print(name[0])
print(name[3])

# Karakter dizilerinde slice işlemi
print(name[0:2])

print("file" in text)


