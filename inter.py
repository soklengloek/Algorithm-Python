class Vehicle:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost
    def show_car(self):
        print("Name of Vehicle:", self.name)
        print("Year of Vehicle:", self.year)
        print("Cost of Vehicle: ${:,.2f}".format(self.cost))
class Car(Vehicle):
    def show_car(self):
        print ("I'm a Car!")
car1 = Car("Toyota Camry", 2020, 24000)
car1.show_car()
