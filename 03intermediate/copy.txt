'''
DRY-> Donot Repeat  Yourself

def function_name(function_parameters):
    function_statements
'''

# function_defination
def greet():
    print("Hello")

# function_calling
# greet()

# greet()

# TODO: parameterised function

# def profile(name,age):
#     print(f"name is {name} and age is {age}")

# profile("John",14)
# n="jane"
# a=12
# profile(n,a)

# TODO: Default function
# NOTE: non-default argument follows default argument
def profile(name="NA",age="NA"):
    print(f"name is {name} and age is {age}")

# profile("jane",14)
# profile("Sam")
# profile()

# profile(13,"John")


# TODO: keyword arguments
# def profile(name="NA",age="NA"):
#     print(f"name is {name} and age is {age}")

# profile(age=13,name="John")

# TODO: variable length arguments
# when you are not aware of no of arguments

def func(*args):
    # print(args)
    # print(type(args))
    count , sum =0 ,0
    for i in args:
        sum=sum+i
        count=count+1
    print("Sum of all elements is: ",sum)
    print("No of elements is :",count)
# func(1,2,34,4,5)
# func()

# TODO: variable length keyword arguments

def func(**kwargs):
    # print(kwargs)
    # print(type(kwargs))

    for k,v in kwargs.items():
        print(f"{k} ---->  {v}")

# func(fname="John",lname="doe",age=18)



# TODO: lambda functions
# anonymous functions

def even(num):
    return num%2==0

# print(even(4))
# function_name = lambda  parameter : expression
is_even = lambda num : num%2==0

# print(is_even(3))

# TODO: return square of a number if it is greater than 0

# sqr = lambda x : x*x if (x>0) else None

# print(sqr(2))
# print(sqr(-5))


# max = lambda a,b : a if(a>b) else b
# print(max(3,5))


# MAP

nums= [1,2,3,4,5,6,7,8,9]

# sqr = list(map(lambda x : x*x , nums))
# print(sqr)

# FILTER 

# odd = list(filter(lambda x : x%2 !=0 , nums))
# print(odd)

# REDUCE

from functools import reduce

sum = reduce(lambda a,b : a+b , nums)
print(sum)

