class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} vehicle is starting...")

    def stop(self):
        print(f"{self.brand} vehicle is stopping...")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def drive(self):
        print(f"{self.brand} {self.model} is driving...")

class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

    def charge(self):
        print(f"{self.brand} {self.model} is charging ({self.battery_capacity} kWh battery)...")

tesla = ElectricCar("Tesla", "Model S", 100)
tesla.start()
tesla.drive()
tesla.charge()
tesla.stop()