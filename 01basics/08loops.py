'''
DRY -> Donot Repeat Yourself

Loops
while loop
for loop
'''

# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")

'''
while loop
initialization
condition
re-initialization(increment/decrement)
'''

# i=1

# while i<=5: 
#     print("Hello ",i)
#     i=i+1

# TODO : WAP to print reverse counting



# i=5

# while i>=1:
#     print(i)
#     i=i-1

# TODO: WAP to print even numbers b/w 0-10

# i = 0

# while i<=10:
#     print(i)
#     i=i+2

# i=0

# while i<=10:
#     if i%2 == 0:
#         print(i)
#     i=i+1


# TODO : for loop
# We execute for loop on iterables(list, string, tuples, dictionary,range)

fruits= ["mango","guava","grapes","apple","kiwi"]

# for i in fruits:
#     print(i)

# name="John"

# for i in name:
#     print(i)

# for num in range(5):
#     print(num)

# 
# while True:
#     print("hello")


# for i in range(5):
#     if i==3:
#         break
#     print(i)
# else:
#     print("loop executed successfully")

for i in range(5):
    if i==3:
        continue
    print(i)
else:
    print("loop executed successfully")