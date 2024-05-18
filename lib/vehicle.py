class Vehicle:
    
    def __init__(self, wheel_size, wheel_number):
        self.wheel_size = wheel_size
        self.wheel_number = wheel_number


    def go(self):
        return "vrrrrrrrooom!"


    def fill_up_tank(self):
        return "filling up!"


my_car = Vehicle("4-passenger seated" , 2)
print(my_car.go())
print(my_car.fill_up_tank())