while True:
  
  a=int(input("enter the number ->"))
  b=int(input("enter the number ->"))
  c=int(input("enter the number ->"))
  if(a>b and a>c):
    print(a," is large")
  elif(b>a and b>c):
    print(b," is large")
  else:
    print(c," is large")  
     
  choice=int(input("press any number for continue and 0 for exit"))
  if choice == 0:
    break