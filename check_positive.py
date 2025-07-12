while True:
 num=int(input("enter a number") )

 if num>0:
    print("positive")
 elif num<0:
    print("negative")
 else:
    print("zero")   

 choice=int(input("press any number for continue and 0 for exit"))
 if choice == 0:
   break