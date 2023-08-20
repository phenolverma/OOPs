class Car(object):
    no_of_tyres=5
    steering_type='Manual'
    def moveCar(self, direction):
        self.direction=direction
        print "Car is Moving towards", self.direction

audi=Car() #Creating an instance of a car class
merc=Car() #creating a new object

#creating new variable for child class
audi.steering_type='Automatic'

print audi.no_of_tyres
print merc.no_of_tyres

print audi.steering_type #Will print Automatic
print merc.steering_type # Will print Manual
print Car.steering_type #Without creating an object , access the attribute of a class called as Statis Attribute or Static Method
audi.moveCar(direction='Left') #Calling a method, by default the object would be passed as an arguement i.e Self
