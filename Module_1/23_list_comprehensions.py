# list comprehension

salaries = [1000, 2000, 3000, 4000, 5000]

def new_salary(x):
    return x * 20 / 100 + x


lis = [new_salary(salary * 2) if salary < 3000 else new_salary(salary) for salary in salaries]
print(lis)


students = ["John", "Mark", "Venessa", "Mariam"]

students_no = ["John", "Venessa"]

new_list = [student.lower() if student in students_no else student.upper() for student in students]

print(new_list)