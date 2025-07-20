import pandas as pd

# Input: number of keys
while True:
    try:
        n = int(input("How many keys?: "))
        break
    except ValueError:
        print(" Please enter digits only, not characters.")


my_dict = {}
for i in range(n):
    print(f"\nKey {i+1}")
    key = input("Enter the key name: ")
    value = input("Enter the values separated by space: ").split()
    # Convert values to int if possible
    change_value = (int(v) if v.isdigit() else v for v in value)
    my_dict[key] = list(change_value)

# Creating DataFrame
df = pd.DataFrame(my_dict)
print("\n✅ Original DataFrame:\n", df)

# Find numeric columns
numeric_cols = df.select_dtypes(include='number').columns

# Add row-wise total if numeric columns exist
if len(numeric_cols) > 0:
    df["total"] = df[numeric_cols].sum(axis=1)
    print("\n✅ DataFrame with Row-wise Total:\n", df)

    #  Apply Statistical Functions:
    print("\n Sum:\n", df[numeric_cols].sum())
    print("\n Mean:\n", df[numeric_cols].mean())
    print("\n Median:\n", df[numeric_cols].median())
    print("\ Mode:\n", df[numeric_cols].mode().iloc[0])  
    print("\n Min:\n", df[numeric_cols].min())
    print("\n Max:\n", df[numeric_cols].max())
    print("\n Std Deviation:\n", df[numeric_cols].std())
    print("\n Variance:\n", df[numeric_cols].var())
    print("\n Full Summary (describe):\n", df[numeric_cols].describe())

else:
    print("\n No numeric columns found to calculate statistics.")
