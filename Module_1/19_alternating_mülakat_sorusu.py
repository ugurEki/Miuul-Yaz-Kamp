## Uygulama / Mülakat Sorusu : Alternating

# Amaç : Aşağıdaki şekilde string değiştiren fonksiyon yazmak istiyoruz.

# before : "hi my name is john and i am learning python"
# after : "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"

string = "hi my name is john and i am learning python"

def convert_string(string):
    new_string = ""
    for st in range(0, len(string)):
        if st % 2 == 0:
            new_string += string[st].upper()
        else:
            new_string += string[st].lower()

    return new_string

print(convert_string(string))
        
