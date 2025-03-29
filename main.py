class Human:
    def __init__(self,name="Human"):
        self.name = name

class Auto:
    def __init__(self,brand):
        self.brand =brand
        self. passengers = []

    def add_passenger(self, human):
            self.passengers.append(human)

    def print_passengers_names(self):
        if self.passengers !=[]:
            print(f"nemes of {self. brand}passemgers:")
            for passenger in self.passengers:
                print(passenger.name)
            else:
                print(f"There are no passenger is {self.brand}")

MA = Human("MA")
Madden = Human("Madden")
Clay = Human("Clay")
car = Auto("BMW")


car.add_passenger(Clay)
car.add_passenger(MA)
car.add_passenger(Madden)
car.print_passengers_names()






