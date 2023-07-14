# Break & Continue & while

salaries = [1000, 2000, 3000, 4000, 5000]

# break
for salary in salaries:
    if salary == 3000:
        print("çalışma durdurulacak")
        break # çalışmayı durdur
    print(salary)

# continue
for salary in salaries:
    if salary == 3000:
        print("pass geç")
        continue # çalışmayı devam ettir
    print(salary)

# while : koşul gerçekleştiği sürece devam et.
number = 1
while number < 5:
    print(number)
    number += 1

    


