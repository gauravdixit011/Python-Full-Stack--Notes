# Python is a Case Sencitive Language

print("Hello") # text/str message
print('Hello Amit') # text/str message
print(5) # integer argument
print(50.5) # float argument
print(True) # boolean argument
# print is function
# function is block of code 

# Basic Data Types
# int - integer   Example 200,350
# float - float   Example 30.5, 102.8
# str   - string  Example "Rakesh", 'Lucknow'
# bool  - boolean Example True, False

# Variable
# Variable stores data in memory.
# Variable is a name for memory address

a=5 
print(a)

name="Rahul"
age=25
salary=45000.70

print("Name: ",name)
print("Age: ",age)
print("Salary: ",salary)

#Rules for Naming  Variable
# 1. Letter(A-Z,a-z), numbers(0-9), underscore(_) allowed
# 2. cannot start with a number
# 3. case sensitive 
# 4. cannot use white space for spaperation
# 5. cannot use reserved keywords => for , if , else , class

# Examples 
# valid : student_name
# valid : marks1
# invalid : 1marks

# get data type/ print data type of a variable
print(type(name))
print(type(age))
print(type(salary))

# Operators
a=5
# Operand => Variable Operand, Literal Operand
# a, 5
# Operator =

# Arithmetic Operators
# + plus addition
# - minus Subtraction
# * asterisk Multiplication
# / forward slash Division
# //  floor division
# ** Exponantial
# % modulus Remainder

a=10
b=3

print(a+b) # 13
print(a-b) # 7
print(a*b) # 30
print(a/b) # 3.33333
print(a//b) # 3
print(a**b) # 10**3= 1000
print(a%b)  # 1 


c=a+b
print("The sum result is:",c)


#2. Assignment Operator =
# a+=2
a=a+2
print(a)

#3. Comparison Operator (Boolean Result)
# ==
# !=
# <
# >
# <=
# >=

a=8
b=8
print(a==b) 

# Conditional Statement
if a==b:
    print("Both are equal")
else:
    print("Not Equal") 

# if
# else
# elif

mark=101
if mark<50:
    print("Fail")
elif mark<60:
    print("Grade D")    
elif mark<70:
    print("Grade C")    
elif mark<80:
    print("Grade B")    
elif mark<=100:
    print("Grade A")    
else:
    print("Cannot exceed")  

  