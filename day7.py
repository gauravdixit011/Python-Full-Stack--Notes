# Function 
# A function is a reusable block of code.
def add():
    a=5
    b=10
    c=a+b
    print(c)

add() # calling function
# A function with parameter. a and b is parameter
def add(a,b):
    c=a+b
    print(c)

d=5
add(d,9) # d and 9 is arguments
add(3,2) # 3 and 2 is arguments

# return function
def add(a,b):
    return a+b

c=add(8,10)

print(c)

# default argument function

def add(a,b=5):
    print(a+b)

add(3) # 8

# arbitary arguments
def add(b,*a):
    print(sum(a)) 

add(4,5,6,7)   

# arbitary keyword arguments

def add(**args):
    print(args)

add(b=2,a=5,c=8,d=44)


# Data Structure
# List
# Tuple
# Set 
# Dictionary

# List
# Features
# Allow Duplicate Value
# Hetrogenous (Allows MIX Data Type)
# Mutable 
x=[1,2,3,4,6]
y=["Apple","Mango","Grapes"]
z=[200.0,300.5,560,3]
a=["Akash",20,"12th","Lucknow",True,1257.23]

a=[] # blank list
a=list() # blank list

a.append(5) # add value to the end of the list
a.append(10)
a.extend([20,2,40])
a.sort() # sort in ascending order
a.sort(reverse=True) # sort in Descending order

# a.clear()
a.reverse()
a.insert(2,"Apple")
a.pop() # remove last value -1
a.pop(0)
a.remove("Apple")


print(a)
print(a+a)
print(a*3)
print(10 in a)

# Tuple
# Allow duplicate value
# Hetrogenous
# immutable
a=(10,20,30,40)
# or
a=10,20,30,40

print(a+a)
print(a*3)
print(10 in a)


