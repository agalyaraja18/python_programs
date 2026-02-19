from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, monthly_salary):
        super().__init__(name, emp_id)
        self.monthly_salary = monthly_salary
    def calculate_salary(self):
        return self.monthly_salary

class Intern(Employee):
    def __init__(self, name, emp_id, stipend, duration_months):
        super().__init__(name, emp_id)
        self.stipend = stipend
        self.duration_months = duration_months
    def calculate_salary(self):
        return self.stipend

emp1 = FullTimeEmployee("Agalya", 101, 50000)
emp2 = Intern("Rahul", 102, 15000, 6)
print(f"{emp1.name} (ID: {emp1.emp_id}) Salary: ₹{emp1.calculate_salary()}")
print(f"{emp2.name} (ID: {emp2.emp_id}) Stipend: ₹{emp2.calculate_salary()}")