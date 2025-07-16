class Student:
    #constructor
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print("Adding new name in DataBase")

 #object
students=[]
n=int(input("select number of student-> "))   
for i in range (n): 
   print(i," number of Data")
   name1=input(" enter your name-> ") 
   marks1=int(input("enter your marks-> "))
   s=Student(name1,marks1)
   students.append(s)
   print("After Data\n","name-> ",s.name,"\n marks-> ",s.marks)

# Display all students data
print("\n======= All Students Data =======")
for student in students:
    student.display()   

