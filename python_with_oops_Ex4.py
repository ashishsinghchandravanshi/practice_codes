import pandas as pd

class Account:
    def __init__(self,Balance,Account_no):
        self.Balance=Balance
        self.Account_no=Account_no

    def debit(self,amount):  
      if amount <=self.Balance:    
        self.Balance-=amount
        print("rs",amount,"is Debited")
      else:
        print("insufficient balance!")  
      print("Total  ",self.get_Balance())

    def credit(self,amount):
        self.Balance+=amount
        print("rs",amount,"is credited") 
        print("Total",self.get_Balance())
    def get_Balance(self):
        return self.Balance  

Balance=int(input("enter Balance: "))
Account_no=int(input("Enter account Number: "))

acc1=Account(Balance,Account_no)
print("Balance is: ",acc1.Balance)
print("Account No. is: ",acc1.Account_no)
while True:
 print("if you want to debit press 1 otherwise press 0 : ")
 choice=int(input("press: "))
 if choice==1:
     n=int(input("enter amount for debit"))
     acc1.debit(n)
 else:
     print("No debit this time. ")
 

 print("if you want to credit press 2 otherwise press 0 : ")   
 choose=int(input("press: "))
 if choose==2:
     m=int(input("enter amount for credit"))
     acc1.credit(m)
 else:
     print("No credit this time. ")  
     
 # Ask if user wants to continue
 c=input("Do you want to continue? (yes/no): ").strip().lower()
 if c== 'yes':
        continue
 else:
        print("Exiting as per user choice.")
        break