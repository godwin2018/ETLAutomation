# OOP FEATURES:
# Inheritance - create new classes based on existing class
# Encapsulation - Bundle class and metho and restrict access using private and protected attribute
# Polymorphism - Multiple forms
# Abstraction - Hiding internal complexity


class Vehicle:
    def __init__(self, brand, model, year):  # this is a constructor
        self.brand_name = brand # can be written as self.brand = brand, self.model_name = model
        print(f'Brand Name is: {self.brand_name}')
        self.model_name = model
        print(f'Model Name is: {self.model_name}')
        self.year_of_manufacture = year
        print(f'Year of Manufacture is: {self.year_of_manufacture}')

    def start_engine(self):
        print(f'Engine Starting')

    def stop_engine(self):
        print(f'Engine Stopping')

'''
V1 = Vehicle('Toyota','Camry','2027')
print(f'Outside Constructor is: {V1.brand_name}')
print(f'Outside Constructor is: {V1.model_name}')

print("==========================")

V2 = Vehicle('Honda','Civic','2012')
print(f'Outside Constructor is: {V2.brand_name}')
print(f'Outside Constructor is: {V2.model_name}')
print(f'Outside Constructor is: {V2.year_of_manufacture}')



# INHERITANCE

class Car(Vehicle):
    def __init__(self, brand, model, year,fuel_type):
        super().__init__(brand,model,year)
        self.fuel_type = fuel_type

    def honk(self):
        print(f'{self.brand_name}, {self.model_name}, {self.year_of_manufacture}, {self.fuel_type}, are for child class')


c = Car('Maruti','Breezer','2028','Petrol')
print(c.fuel_type)
c.start_engine()
c.stop_engine()
c.honk()

v = Vehicle('Tesla','Model S','2030')
v.start_engine()
v.stop_engine()

'''

# ENCAPSULATION
# public - everyone can access
# protected - only child class can access (denoted by single underscore)
# private - Can only be access inside the class only (denoted by double underscore)

# It more for security purpose

class BankAccount:
    def __init__(self, owner, balance, pin):
        self.owner = owner
        print(f'Printing inside constructor {self.owner}')
        self._balance = balance
        print(f'Printing inside constructor {self._balance}')
        self.__pin = pin
        print(f'Printing inside constructor {self.__pin}')


    def display(self):
        print(f'Printing inside class {self.owner}')
        print(f'Printing inside class {self._balance}')
        print(f'Printing inside class {self._BankAccount__pin}') # name mangling


class SavingsAccount(BankAccount):
        def __init__(self, owner, balance, pin,interest_rate):
            BankAccount.__init__(self, owner, balance, pin)
            #super().__init__(owner,balance,pin) # you either use super or use the parent name direct
            self.interest_rate = interest_rate




        def accessparentaccont(self):
            print(f'owner is: {self.owner}')
            print(f'balance is: {self._balance}')
            print(f'interest rate is: {self.interest_rate}')





# create an object of the account

bank = BankAccount('Zane','£1000','2345')
print(bank.owner)
print(bank._balance)
bank.display()
print(bank._BankAccount__pin)
print('=================')
b2 = SavingsAccount('Ziv',1000,'3289',0.74)
print(b2.interest_rate)
b2.accessparentaccont()
