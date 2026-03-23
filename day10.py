# Operator Overloading
a=5
b=10
print(a+b) # 15
# But for strings
s1="Hello"
s2="World"
print(s1+s2) # HelloWorld
# + operator is overloaded to perform addition for numbers and concatenation for strings.
# We can overload operators in our own classes too.
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    # Overloading + operator
    def __add__(self,other):
        return Point(self.x+other.x,self.y+other.y)

p1=Point(2,3)
p2=Point(4,5)
p3=p1+p2
print(p3.x,p3.y) # 6 8 

# + __add__ for addition
# += __iadd__ for in-place addition
# - __sub__ for subtraction
# -= __isub__ for in-place subtraction
# * __mul__ for multiplication
# / __truediv__ for division
# == __eq__ for equality
# < __lt__ for less than
# > __gt__ for greater than
# etc.

# Class vs Instance Variable
class Car:
    wheels=4 # Class variable (shared by all objects)
    def __init__(self,make):
        self.make=make # Instance variable (unique to each object)

    @classmethod
    def change_wheels(cls,num):
        cls.wheels=num    


c1=Car("Toyota")
c1.change_wheels(6) # Changing class variable using class method
c2=Car("Honda")
print(c1.make,c1.wheels) # Toyota 4
print(c2.make,c2.wheels) # Honda 4        

# Static Method & Class Method

class Math:
    @staticmethod
    def add(a,b):
        return a+b

    @classmethod
    def info(cls):
        print("This is a Math class")
        print("Class Name:",cls.__name__)
       
print(Math.add(5,10)) # 15
Math.info() # This is a Math class

# Real World Example of OOPs
class ATM:
    def __init__(self,balance):
        self.balance=balance
    def deposite(self,amount):
        self.balance+=amount
        print("Amount Deposited:",amount)
    def withdraw(self,amount):   
        if amount>self.balance:
            print("Insufficient Balance")
        else:
            self.balance-=amount
            print("Amount Withdrawn:",amount)
    def check_balance(self):
        print("Current Balance:",self.balance)        

atm=ATM(1000)
atm.check_balance() # Current Balance: 1000
atm.deposite(500) # Amount Deposited: 500
atm.check_balance() # Current Balance: 1500
atm.withdraw(200) # Amount Withdrawn: 200
atm.check_balance() # Current Balance: 1300
atm.withdraw(1500) # Insufficient Balance
atm.check_balance() # Current Balance: 1300





