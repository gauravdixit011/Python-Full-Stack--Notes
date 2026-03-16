# match case 

dayNumber=9

match dayNumber:
    case 1:
        print("Sun")
    case 2:
        print("Mon")    
    case 3:
        print("Tue")    
    case 4:
        print("Wed")    
    case 5:
        print("Thu")    
    case 6:
        print("Fri")  
    case 7:   
        print("Sat")
    case _:
        print("Day Number Invalid")    

# Example 1: Simple Number Match
num=2

match num:
    case 1:
        print("One")
    case 2:
        print("Two")    
    case _:
        print("Other Number")    

# Example 2: Day of Week
day="Monday" 

match day:
    case "Monday":
        print("Start of Week")
    case "Friday":
        print("Weekend Coming")  
    case _:
        print("Normal Day")    

# Example 3: Grade System

grade="A"        

match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Good")    
    case "C":
        print("Average")    
    case _:
        print("Needs to Improvement")    

# Example 4: Even or Odd
num=7
match num%2:
    case 0:
        print("Even")        
    case 1:
        print("Odd")    

# Example 5: Traffic Light
signal="red"

match signal:
    case "red":
        print("Stop")
    case "yellow":
        print("Ready")    
    case "green":
        print("Go")    

# Example 6: Menu Selection
choice =1
match choice:
    case 1:
        print("Pizza")
    case 2:
        print("Burger")    
    case 3:
        print("Pasta")  

# Example 7: Month Categories
monthNumber=12
match monthNumber:
 case 12|1|2:
        print("Winter")
 case 3|4|5:
        print("Summer")       
 case _:
        print("Rainy")       

# Example 8: Vowel or Consonants
char="O"

match char:
    case "A"|"E"|"I"|"O"|"U":
        print("Vowel")
    case _:
        print("Consonant")    

# How to user input from console


# Example 9: Login Role 

# role=input("Enter your Login Role: ") # string input by default

# match role:
#     case "admin":
#         print("Full access")
#     case "user":
#         print("Limited access")
#     case _:
#         print("Guest access")   

# Loop : Iterarion
# Loops repeat a block of code/ repeat a same task.
# Two main loops:
# for
# while

# For Loop
# Used when the number of repeatition is known.

# Example  with numeric range
for x in range(1,6): # 1,2,3,4,5
    print(x)

# Example with string
for s in "ajay":
    print(s)

# square star pattern way 1 
for x in range(1,6):
    print("* "*5)

print("--------------------")

# square star pattern way 2
for x in range(1,6):
    for y in range(1,6):
        print("*",end=" ")
    print()   

# number pattern 1
for i in range(1,6):
    print((str(i)+" ")*5)     

# While Loop:

# Used when the condition controls repetition.

i=1
while i<=5:
    print(i)
    i+=1





# Sum of number
# 1-10  sum
i=1
sum=0

while i<=10:
    sum+=i
    i+=1

print("Sum of 1-10 numbers is :",sum)

# Guess Password
password=""

while password!="admin":
    password=input("Enter  Your Password:")

print("Great You Guess the password ")


