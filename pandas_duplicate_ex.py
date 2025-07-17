import pandas as pd
n=int(input("how many keys"))
my_dict={}
for i in range(n):
    key=input("enter key name: ")
    value=input("enter value seprated by space: ").split()
    change_value=(int (v) if v.isdigit() else v  for v in value)
    my_dict[key]=list(change_value)
    
df=pd.DataFrame(my_dict)
print(df)

c=int(input("press 1 if you want Find duplicate value otherwise press 0: "))
if c==1:
    res=df.duplicated()
    print("\ndescribing duplicates\n",res)
else:
    print("original dataframe",df)
choice=int(input("press 1 if you want remove duplicate value otherwise press 0: "))
if choice==1:
    result=df.drop_duplicates()
    print("\nremove duplicates\n",result)
else:
    print("original dataframe",df)