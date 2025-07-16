class Student:
    #constructor
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print("Adding new name in DataBase")

 #object
n=int(input("select number of student-> "))   
for i in range (n): 
   print(i," number of Data")
   name1=input(" enter your name-> ") 
   marks1=int(input("enter your marks-> "))
   s1=Student(name1,marks1)
   print("After Data\n","name-> ",s1.name,"\n marks-> ",s1.marks)

