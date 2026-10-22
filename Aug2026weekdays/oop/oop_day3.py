# Method overloading - this is not encouraged in Python
'''
# problem path
class Maths:
    def addition(self, a, b):
        return a + b

    def addition(self, a, b,c):
        return a + b + c

    #def subtraction(self, a, b):

obj = Maths()
sum1 = obj.addition(2,3,4)
print(sum1)
sum2 = obj.addition(2,3)
print(sum2)

# solution path
class Maths:
    def addition(self, a, b,c=0,d=0):
        return a + b + c

    #def subtraction(self, a, b):

obj = Maths()
sum1 = obj.addition(2,3,4)
print(sum1)
sum2 = obj.addition(2,3)
print(sum2)
sum3 = obj.addition(7,3,6,9)
print(sum3)

# It will always call the last method if you have two methods


# Method overriding - is using the same method is parent and child class

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model

    def start(self):
        print("Vehicle is starting")

    def stop(self):
        print("Vehicle is stopping")


class Car(Vehicle):
    def honk(self):
        print("Car is honking")

    def start(self):
        print("Car is kicking")


c = Car()
c.start()
c.stop()
c.honk()
print('---------------')
v = Vehicle()
v.start()
v.stop()


# Operator overloading
class OperatorOverloading:
    def __init__(self, num1,num2,str1,str2):
        self.num = num1+num2
        self.concat_str = str1 + str2

    def printMethod(self):
        print(self.num)
        print(self.concat_str)


o = OperatorOverloading(10,20,'Zane','Ziv')
o.printMethod()
#o2 = OperatorOverloading(10,20,50,50)
o2 = OperatorOverloading(10,20,'50','50')
o2.printMethod()


# Class overloading

class Circle:
    def area(self):
        return 3.14*5*5

class Square:
    def area(self):
        return 5*5

class Triangle:
    def area(self):
        return 0.5*5*4

c = Circle()
s = Square()
t = Triangle()
shapes = [c,s,t]

for obj in shapes:
    print(obj.area())



# Abstraction - it is hiding complexity of the system to end user
# We can achieve that using the abstract class and abstract method

# Abstract Class: We cannot create an object of an abstract class

# Abstract Method - This method has missing implementation

class Vehicle: # This is a concrete class
    def start(self):
        print("Vehicle is starting")

    def stop(self):
        print("Vehicle is stopping")


v = Vehicle()
v.start()
v.stop()
'''

# Abstract class
# To have an abstract class, you will need to inherite an abstract class from Python
from abc import ABC, abstractmethod
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def honk(self):
        print("Vehicle is honking")


class Car(Vehicle):

    def start(self):
        print("Car is starting")

    def stop(self):
        print("Car is stopping")


class Bike(Vehicle):
    def start(self):
        print("Bike is starting")

    def stop(self):
        print("Bike is stopping")

c = Car()
c.start()
c.stop()
c.honk()

b = Bike()
b.start()
b.stop()
b.honk()

