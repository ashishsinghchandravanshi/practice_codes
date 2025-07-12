d = {"a": 1, "b": 2}
item = d.popitem()
print(item)  # ('b', 2)
print(d)     # {'a': 1}
#nested dictionary
student = {
    "name": "Ravi",
    "age": 20,
    "marks": {
        "math": 85,
        "science": 90
    }
}

print(student)
#loop through 
d = {"a": 1, "b": 2, "c": 3}

for key in d:
    print(key)

# or explicitly
for key in d.keys():
    print(key)
    #loop through values
for value in d.values():
    print(value)

