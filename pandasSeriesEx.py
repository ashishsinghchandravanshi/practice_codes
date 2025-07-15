import pandas as pd
n=int(input("how many index"))
Data=[]

for i in range(n):
    values=input("enter the values")
    Data.append(values)
s=pd.Series(Data,name= "pandas series")
print("\n series is-> \n", s.dtype)
print("\n number of dimension is-> \n  ",s.ndim)
print("\n Name of series is -> \n",s.name)
print("\n index of series is -> \n",s.index)
print("\n head of series - > \n", s.head())
print("\n tail of series -> \n ",s.tail())
print("\n info of series -> \n ",s.info())
