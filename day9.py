# OOPs (Object Oriented Programings) Programming
# OOPs ogranizes programs using objects and classes.
#  Key Concepts
# 1. Class
# 2. Object
# 3. Inheritance
# 4. Encapsulation
# 5. Polymorphism
# 6. Abstraction

#1. Creating a class
class Student:
    def show(self): 
        print("Student object Created")

#2. Creating Object
s1 = Student()
# calling function by object
s1.show()

# 3. Constructor (__init__)
class Student: 
    def __init__(self,name,age):
        self.name=name
        self.age=age
# Notes: self means current object
s1=Student("Gaurav",22)   
s2=Student("Akash",21)

print(s1.name,s1.age)
print(s2.name,s2.age)

# 4. Instance Method
# Functions inside a class
class Student:
    # Constructor
    def __init__(self,name):
        self.name=name
    # Instance Method
    def display(self):
        print("Student Name:",self.name)   

s1=Student("Arjun")
s1.display()


# 5. Encapsulation
# Wrapping data + methods together and controlling access.
# Public, Protected, Private
class Bank:
    def __init__(self):
        self.name="Gaurav" # Public
        self._balance =50000 # Protected
        self.__pin =1234 # Private

b=Bank()
print(b.name)
print(b._balance)
# print(b.__pin) ❌ Error
# Private variables cannot be accessed directly

# 6. Inhertance
# One class inherts another

class Parent:
    def show(self):
        print("Parent Class")

# Apply Inheritance
class Child(Parent):
    def display(self):
        print("Child Class")       

c=Child()
c.show()
c.display()

# 7. Polymorphism
# Same function Name, different behavior.

# Method Overriding
class Animal:
    def sound(self):
        print("animal can sound") 

class Dog(Animal):
    # Method Override
    def sound(self):
        print("Bark")

class Cat(Animal):
    # Method Override
    def sound(self):
        print("Meow")

# 8. Abstraction
# Hide internal details, show only essential features
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass 
class Circle(Shape):
    def area(self):
        print("Area of Circle")
c=Circle()
c.area() 
# Can't instantiate abstract class Shape 
# without an implementation for abstract method 'area' 
s=Shape()      




