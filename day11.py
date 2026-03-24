# Exception Handling
# Errors can crash Programs. Python allows handling them safely.

# Syntax:

# try:
#   code
# except:
#   error handling  

# Example : Multiple Exception
# try:
#  num = int(input("Enter Number: "))
#  print(10/num)
# except ValueError as e:
#  print("Invalid Type Input Please Input Integer Value") 
# except ZeroDivisionError as e:
#  print("Cannot Divide by Zero") 

# Example : Multiple Exception in One Block
# try:
#  num = int(input("Enter Number: "))
#  print(10/num)
# except (ValueError,ZeroDivisionError) as e:
#  print("Error: ",e) 

# Example : else Block (Success Case)
# try:
#  num = int(input("Enter Number: "))
#  print(10/num)
# except (ValueError,ZeroDivisionError) as e:
#  print("Error: ",e) 
# else:
#  print("Execution Successful") 

#Example : Finally Block (Always Runs) 
# try:
#  f=open("file.txt")
#  print(f.read())
# except FileNotFoundError:
#  print("File Not Found")
# finally:
#  print("Closing Program") 

# Example : Raising Exceptions

# age=int(input("Enter age:"))
# if age<18:
#     raise Exception("Not Eligible")
# else:
#     print("Eligible")

# Example Custom Exception Class
# class InvalidAmountError(Exception):
#     pass

# amount=int(input("Enter Amount:"))

# if amount<0:
#     raise InvalidAmountError("Amount Cannot be Negative")


# File Handling

# Write File
file=open("data.txt","w") 
# w mode re-write  the content
# a mode append the content
file.write("Hi Hello")
file.close()

# Read File
file=open("data.txt","r")
print(file.read())
file.close()


