import pandas as pd
import numpy  as np
from pandas.api.types import is_numeric_dtype
n=int(input("how many keys"))
my_dict={}
for i in range(n):
    key=input("enter key name: ")
    value=input("enter value seprated by space: ").split()
    change_value = (
        int(v) if v.isdigit() else np.nan if v.lower() == 'nan' else v for v in value
    )
    my_dict[key]=list(change_value)
    
df=pd.DataFrame(my_dict)
print("original dataframe:", df)

c=int(input("press 1 if you want fix null value mean method otherwise press 0: "))
if c==1:
  df_fixed=df.copy()  
  for col in df_fixed.columns:
     if is_numeric_dtype(df_fixed[col]):
        mean_value=df_fixed[col].mean()
        df_fixed[col]= df_fixed[col].fillna(mean_value)

     else:
        mode_value=df_fixed[col].mode()
        if not mode_value.empty:
           df_fixed[col]=df_fixed[col].fillna(mode_value[0])

    
  print(df_fixed)
else:
   print(df)