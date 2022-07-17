# this is a parent class
class Vehicle:
    def __int__(self, make, model, fuel):
        self.make = make
        self.model = model
        self.fuel = fuel


# child class inheriting parent
class Car(Vehicle):
    def __int__(self, make, model, fuel, ac, sunroof):
        Vehicle.make = make
        Vehicle.model = model
        Vehicle.fuel = fuel
        self.ac = ac
        self.sunroof = sunroof


if "__name__" == '__main__':
    obj1 = Car('Tesla', '2008', 'Electric', 'Yes', 'Yes')
    obj1.__dict__()