class Vehicle(object):
    def __init__(self):
        print("Vehicle")

class Car(Vehicle):
    def __init__(self):
        super(Car,self).__init__()
        print("Car")

c= Car()
