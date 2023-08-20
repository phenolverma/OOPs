from myCar import Car
class Eurocar(Car):
    def moveCar(self, direction):
        self.direction=direction
        print "EuroCar is Moving towards", self.direction
        super(Eurocar,self).moveCar(direction)
class AmericanCar(Car):
    def moveCar(self, direction):
        self.direction=direction
        print "American is Moving towards", self.direction
        super(AmericanCar,self).moveCar(direction)
class IndianCar(Eurocar,AmericanCar):
    pass

audi=IndianCar()
print audi.moveCar(direction='Right')