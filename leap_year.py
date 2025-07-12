while True:
  year=int(input("enter a year"))
  if(year%4==0) and (year%100!=0 or year%400==0):
    print(year,"leap year")
  else:
    print("not a leap year")  
  choice=int(input("for cotinue press button and for break break 0"))  
  if choice ==0:
    break