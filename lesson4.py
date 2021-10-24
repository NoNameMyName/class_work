from datetime import datetime

class Car:
    car_count = 0

    def __init__(self, year=2013, make="Honda", model="CRV"):
        Car.car_count +=1
        print(Car.car_count)
        self.year = year
        self.make = make
        self.model = model

    @staticmethod
    def get_date():
        return datetime.now()

    @staticmethod
    def get_car_deteils(year):
        print("Этот класс Car")
        return "Declined" if year < 2000 else "In progress"

    def start(self):
        print(f"Я завёл {self.make} {self.model} {self.year} года, сегодня в {self.get_date()}")
        status = self.get_car_deteils(self.year)
        print(status)

car_b = Car(2021, "Mersedes", "GLS")
car_b.start()
car_a = Car()
car_a.car_count = 10
print("car_a.car_count:", car_a.car_count)
