import pandas as pd
n=int(input("how many keys -> "))
my_dict={}
for i in range(n):
    key=input("enter key name: ")
    values=input("enter value (like when need  city*100) seprated by space").split()
    final_values=[]
    for v in values:
        if "*" in v:
           item_name,count=v.split("*")
           final_values.extend([item_name]*int(count))
        else:
            final_values.append(int(v) if v.isdigit() else v )
    my_dict[key]=final_values
print(my_dict)

df=pd.DataFrame(my_dict)
print("before categorial",df)
print( "info",df.info(memory_usage="deep"))

#after categorical 
for col in df.columns:
    df[col]=pd.Categorical(df[col])
print("after categorial ",df) 
print("info ",df.info(memory_usage="deep"))   