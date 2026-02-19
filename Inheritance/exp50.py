class Employee:
    def __init__(self, salary, bonus):
        self._salary = salary
        self.__bonus = bonus

    def get_bonus(self):
        return self.__bonus

class Manager(Employee):
    def display_details(self):
        print("Salary:", self._salary)

mgr = Manager(50000, 10000)
mgr.display_details()
print("Bonus (via method):", mgr.get_bonus())
