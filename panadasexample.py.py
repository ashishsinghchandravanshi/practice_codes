import pandas as pd
n=int(input("How many keys "))
my_dict={}
for i in range(n):
   
   keys=input("enter the key ")
   value=input("enter the value seprated by space ").split()
   change_value=(int(v) if v.isdigit() else v for v in value) # in this () is called geneartor
   my_dict[keys]=list(change_value) # when use generator then define it is list,tuple,or set
   print(my_dict)
choice = input("Do you want to give row names? (yes/no): ").strip().lower() # for remove extra spaces

if choice == "yes":
    row = input("Enter names of index separated by space: ").split()
    df = pd.DataFrame(my_dict, index=row)
else:
    df = pd.DataFrame(my_dict)

print(df)    

print("this is for  remove index",df.to_string(index=False))
print("with index\n",df.size) # use for remove  index when print and size
print("for shape\n",df.shape)
print("first 5 rows \n ",df.head())
print("Last 5 rows \n ",df.tail())
print("transpose\n",df.T)









