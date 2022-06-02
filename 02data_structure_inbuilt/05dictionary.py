'''
dictionary -> {}
{key : value}
ordered
mutable
iterable
keys can be immutable datatype -> int, strings, tuples
any datatype can be a value for the key
'''

stu = {
    "fname":"John",
    "lname" : "Doe",
    "gen":"M",
    "course": "Python"
}
# print(stu)

# print(stu['fname'])
# print(stu['lname'])

# stu['contact']="2324355"
# print(stu)

# print(stu.items())
# print(stu.keys())
# print(stu.values())


for k , v in stu.items():
    print(f"key is : {k} and value is : {v}")

