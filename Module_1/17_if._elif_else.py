# if 
if 1 == 1:
    print("something")

number = 11
if number == 11:
    print("True")

def number_check(number):
    if number == 11:
        print("number is 10")

# else
def number_check(number):
    if number == 11:
        print("number is 10")
    else:
        print("number is not 10")

# elif 
def number_check(number):
    if number > 10:
        print("greater than 10")
    elif number < 10:
        print("less than 10")
    else:
        print("equal to 10")

number_check(10)