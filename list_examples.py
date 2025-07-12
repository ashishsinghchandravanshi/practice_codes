list=input("enter an element seperated by space  ").split()
print(list)
print("negative slice",list[4:0:-1])

app=input("enter element to append")
list.append(app)
print(list)  

index = int(input("Enter index where you want to insert: "))
element = input("Enter element to insert: ")
list.insert(index, element)
print("After insert:", list)

val=input("enter a number to remove")
if val in list:
    list.remove(val)
    print("remove",list)
else:
    print(val ,"not found in list")   

p=input("for pop press1 ")
if p=="1":
   list.pop(p)
   print("pop ex",list)
else:
    print("invalid choice") 
         #in this last element will be delete
list.sort()
print("sort",list)

list.reverse()
print("reverse",list)
