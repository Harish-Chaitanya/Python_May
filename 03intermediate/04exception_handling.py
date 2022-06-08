'''
Error

syntax error ->
logical error -> 2 + 2  '2' + '2' =22
runtime error 

exception handling is a method which handles potentially occuring errors gracefully
'''

# n1=4
# n2=0
# try:
#     print(n1/n2)

# except ZeroDivisionError as e:
#     print(e)
#     print("denominator should not be 0")

# print("100 lines of code")

# try:

#     # with open('abc.txt','r') as f1:
#     #     print("Success")
#     # print(a)
#     print("7")

# except FileNotFoundError as e:
#     print(e)

# except BaseException as e:
#     print(e)

# else:
#     print("else block executes when there is no exception")

# finally:
#     print("No matter what , it always gets executed")


# name="john"

# if name =="john":
#     raise ValueError("Not allowed")


def func():
    try: 
        return 1
    except :
        return 2
    else:
        return 3
    finally:
        return 4
print(func())