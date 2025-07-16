#Create student class that takes name and calculate the average marks of subjects

class Student:

    def __init__(self,name,subjects,marks):
        self.name=name
        self.subjects=subjects
        self.marks=marks

    
    def avg_marks(self):
        total=0
        for v in self.marks:
           total=v+total
        avg=total/len(self.marks)
        print(f"Average marks of {self.name}: {avg}")


    def display(self):
        print(f"student name: {self.name},")
        for sub,mark in zip(self.subjects,self.marks):
            print(f"subject: {sub},marks: {mark}")
        
x=int(input("how many students"))
for u in range(x):
  name=input("enter your name-> ")
  n=int(input("how many subject?:  "))
  subjects=[]
  marks=[]
  for i in range(n):
    sub=input(f"enter your subject {i+1} name-> ")
    mark = int(input(f"Enter marks for {sub} -> "))
    subjects.append(sub)
    marks.append(mark)
    s=Student(name,subjects,marks)    
  print("\n--student display----- ")
  s.display()

  print("\n---average marks----")
  s.avg_marks()