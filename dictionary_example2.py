keys=input("enter key seprated by space").split()    #when we need to take waithout space then use list like list(input())
values=input("enter value seprated by space").split()
#[true_val if condition else false_val for item in iterable]it is ternary expression 
covertedvalues=(int(v) if v.isdigit() else v for v in values )
my_dict=dict(zip(keys,covertedvalues))
print(my_dict)