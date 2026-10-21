# print hello 10 times

# Procedural way
'''
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")



# Functional way

def print_hello():
    print("Hello World")
    print("Hello World")
    print("Hello World")
    print("Hello World")
    print("Hello World")
print_hello()
print_hello()


# Object Oriented Programming way

class PrintClass:

    name = 'Godwin'
    def print_hello(self):
        print("Hello World")
        print("Hello World")
        print("Hello World")
        print("Hello World")
        print("Hello World")

    def print_bye(self):
        print("Goof Bye")

#PrintClass().print_hello()
#PrintClass().print_bye()
#PrintClass().print_hello()

# It is better to create an object of that class before you call the class
obj1 = PrintClass()

obj1.print_hello()
obj1.print_bye()
obj1.name
var_name = obj1.name
print(var_name)
print(obj1.name)
print(type(obj1.name))
print(obj1)

# What is a class? It is a blueprint, design, plan, model that defines a set of attributes (data or variable) and methods that object created from the class.
# What is an object? It is the instance of the physical existence of a class
# Class is the plan and object is the real thing.
# You have to create an object for the class to be used




# A class contains a method/function and an attribute



class Car:
    def start(self):
        print("Car Starts")

    def stop(self):
        print("Car Stops")

    color = 'Black'
    seating_capacity = 4

car1 = Car()
car1.start()
car1.stop()
colr = car1.color
print(colr)
seating = car1.seating_capacity
print(seating)


# constructor

class Car:
    def __init__(self):
        pass

    def start(self):
        print("Car Starts")

    def stop(self):
        print("Car Stops")

    color = 'Black'
    seating_capacity = 4

    c1 = Car()
    c1.start()
    c1.stop()


# Put the variable into the constructor

class Car:
    def __init__(self, color, seating_capacity):
        print('This is a constructor')
        color = 'Black'
        seating_capacity = 4

    def start(self):
        print("Car Starts")

    def stop(self):
        print("Car Stops")

'''
# Making the un from the constructor

class Car:
    def __init__(self, color, seating_capacity, car_type):
        print('This is a constructor')
        self.color = color
        self.seating_capacity = seating_capacity
        self.car_type = car_type

    def start(self):
        print("Car Starts")

    def stop(self):
        print("Car Stops")

c1 = Car('Black', 4,'SUV')
print(c1.color)
print(c1.seating_capacity)
print(c1.car_type)

c2= Car('Red', 6, 'Sedan')
print(c2.color)
print(c2.seating_capacity)
print(c2.car_type)
