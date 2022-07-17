class Vehicle():
    def __int__(self,make,model,fuel):
        self.make = make
        self.__model = model
        self.__fuel = fuel

#     def __private_method_parent(self):
#         print("This is private")
#
# class Car(Vehicle):
#     def __int__(self,make,model,fuel,air_cond,sunroof):
#         super(Car,self).__int__(make,model,fuel)
#         self.air_cond = air_cond
#         self.sunroof = sunroof
#
#
# myobj = Car('Tesla','2019','Electric',True,True)
# myobj.__dict__
#

# Parent Class
class Vehicle():
    def __init__(self, make, model, fuel):
        self.make = make
        self.__model = model
        self.__fuel = fuel

    def __private_method_parent(self):
        print("This is private")


# Child Class
class Car(Vehicle):
    def __init__(self, make, model, fuel, air_conditioning, sunroof):
        super(Car, self).__init__(make, model, fuel)
        self.air_conditioning = air_conditioning
        self.sunroof = sunroof


myobj = Car("Tesla", 2019, "Electric", True, True)

myobj.__dict__
# myobj.make
