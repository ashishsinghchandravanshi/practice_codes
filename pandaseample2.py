#join dataframe  example

import pandas as pd 
n=int(input("how many keys-> "))
my_dict1={}
for i in range(n):
    keys=input("enter the name of keys-> ")
    value=input("enter the values->  ").split()
    changevalue=(int(x) if x.isdigit() else x for x in value)
    my_dict1[keys]=list(changevalue)
print(my_dict1)    
df1=pd.DataFrame(my_dict1)

#df.to_csv(r"D:\python\my_data.csv",index=True) it is use for save
print("1st dataframe\n",df1)
num=int(input("how many key"))
my_dict2={}
for i in range(num):
    Key2=input("enter the name of keys ")
    value2=input("enter the name of value seprated by space ").split()
    changevalues=(int(v) if v.isdigit() else v for v in value2)
    my_dict2[Key2]=list(changevalues)
print(my_dict2)
df2=pd.DataFrame(my_dict2) 
print("2nd dataframe\n",df2)

df3=df1.join(df2)
print("after join \n",df3)

   
