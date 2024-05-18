from vehicle import Vehicle  #configuration

#subclass of Vehicle
#Car class inherit all of the Vehicle attributes and methods and therefore have access to them. 
class Car(Vehicle):
    # overwrite the inherited go() method with one specific to Car.
    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"


my_car2 = Car("bigggg" , 3)
print(my_car2.go())
print(Car.__bases__)  # (<class 'vehicle.Vehicle'>,) => returns tuple, parent classess of Car class
