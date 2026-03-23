class Student:
    def __init__(self,roll_no,name,age,course):
      self.roll_no=roll_no
      self.name=name
      self.age=age
      self.course=course
    def display(self):
       print("Roll Number:",self.roll_no,", Name:",self.name,", Age:",self.age,", Course:",self.course)


class StudentManagement:
   def __init__(self):
      self.students=[]

   # add student
   def add_student(self):
      roll=int(input("Enter Roll Number:"))
      name=input("Enter Name:")
      age=int(input("Enter Age:"))   
      course=input("Enter Course")

      student=Student(roll,name,age,course)
      self.students.append(student)
      print("✔️ Student added Successfully")

   def view_students(self):
      if not self.students:
         print("❌ No Student record found")   
         return
      for student in self.students:
         student.display()
      print()
   def search_students(self):
      roll=int(input("Enter Roll Number to Search:"))      
      for student in self.students:
         if student.roll_no==roll:
            student.display()
            return 
      print("❌ Student Not Found")   

   def delete_student(self):    
      roll=int(input("Enter roll number to delete:"))
      for student in self.students:
         if student.roll_no==roll:
            self.students.remove(student)
            print("✔️ Student record Deleted")
            return
      print("❌ Student Not Found")   
   def update_student(self):
      roll=int(input("Enter roll number to Update:"))   
      for student in self.students:
         if student.roll_no==roll:
            student.name=input("Enter Name:")
            student.age=int(input("Enter Age:"))
            student.course=input("Enter Course:")
            print("✔️ Student Record Updated")
            return 
      print("❌ Student Not Found")   


def main():
   system=StudentManagement()

   while True:
      print("====== Student Management System ======")
      print("1. Add student")
      print("2. View Students")
      print("3. Search Student")
      print("4. Delete Student")
      print("5. Update Student")
      print("6. Exit")

      choice=int(input("Enter Your Choice:"))

      match choice:
         case 1:
            system.add_student()
         case 2:
            system.view_students()
         case 3:
            system.search_students()
         case 4:
            system.delete_student()
         case 5:
            system.update_student()
         case 6:
            print("Exiting... Goodbye 👋")   
            break
         case _:
            print("Invalid Choice")

if __name__=="__main__":
   main()            
