class Human:
    def __init__(self, name="Human"):
        self.name = name


class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passenger(self, *args):
        for passenger in args:
            self.passengers.append(passenger)

    def print_passenger_names(self):
        if self.passengers != []:
            print("Names of ", self.brand, " passengers:")
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print("No passengers")


man1 = Human(name="Jack")
man2 = Human(name="Nik")
man3 = Human(name="Bob")
car = Auto("BMW")
car.add_passenger(man1, man2, man3)
car.print_passenger_names()
