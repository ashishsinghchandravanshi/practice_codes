while True:

 marks = int(input("Enter your marks: "))

 if marks >= 90:
     print("Grade: A+")
 elif marks >= 80:
     print("Grade: A")
 elif marks >= 70:
     print("Grade: B")
 elif marks >= 60:
     print("Grade: C")
 elif marks >= 50:
     print("Grade: D")
 else:
     print("Fail")
 choice=int(input("for cotinue press button and for break break 0"))  
 if choice ==0:
    break