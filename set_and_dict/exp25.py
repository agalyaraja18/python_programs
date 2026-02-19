employee_salaries = {}
num_entries = int(input("Enter the number of entries: "))
for _ in range(num_entries):
    key = input("Enter a key: ")
    value = input("Enter a value: ")
    employee_salaries[key] = value
print(employee_salaries)
highest_paid_salary=max(employee_salaries, key=employee_salaries.get)
highest_salary=employee_salaries[highest_paid_salary]
print("The highest paid employee is",highest_paid_salary)
print("The highest salary is", highest_salary)
