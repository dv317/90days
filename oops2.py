class Vehicle():
    def __int__(self, make, fuel, model):
        self.make = make

        # private
        self.__model = model
        self.__fuel = fuel

    def __private_method_parent(self):
        print('This is Private')


class Car(Vehicle):
    def __init__(self, model, make, fuel, air_cond, roof):
        Vehicle.make = make
        Vehicle.__model = model
        Vehicle.__fuel = fuel

        self.air_cond = air_cond
        self.roof = roof

    def show_parent_attribute(self):
        print (Vehicle.make, ' ', Vehicle.__model,' ', Vehicle.__fuel)

    def show_private_method_attribute(self):
        self._Vehicle.__private_method_parent()

myobj = Car("Tesla","2019","Electric",True,True)
myobj.show_parent_attribute()
myobj.show_private_method_attribute()