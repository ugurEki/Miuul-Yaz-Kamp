# for loop

students = ["John", "Mark", "Venessa", "Mariam"]

for student in students:
    print(student.upper())

salaries = [1000, 2000, 3000, 4000, 5000]

def zamli_maas(salaries, zam_miktari = 10):
    zamli_maaslar = []
    for salary in salaries:
        zamli_maaslar.append(int(salary * zam_miktari/100 + salary))
    return zamli_maaslar

print(zamli_maas(salaries, zam_miktari=50))

def yeni_maaslar(salaries):
    outputs = []
    for salary in salaries:
        if salary >= 3000:
            print("Salary {} is going to increase 15 %".format(salary))
            outputs.append(int(salary * 15/100 + salary))
        elif salary >= 2000:
            print("Salary {} is going to increase 25 %".format(salary))
            outputs.append(int(salary * 25/100 + salary))
        else:
            print("Salary {} is going to increase 5 %".format(salary))
            outputs.append(int(salary * 5/100 + salary))
    return outputs

print(yeni_maaslar(salaries))

