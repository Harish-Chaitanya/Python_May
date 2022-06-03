# TODO: list comprehension

nums = [1,2,3,4,5,6]

# nums = [i for i in range(1,7)]
# print(nums)

# TODO: using if condition
# even = [i for i in range(11) if i%2==0]
# print(even)

# l1 = [i for i in range(101) if (i%2==0 and i%5==0) ]
# print(l1)

# nums =[i**2 if i%2==0 else i**3 for i in range(10)]
# print(nums)


# mat = [[ j for j in range(4)]for i in range(3)]
# print(mat)

# TODO : dictionary comprehension
# {k:v for k,v in iterable}

# print({i: i**2 for i in range(5)})

keys=['a','b','c','d','e']
values=[1,2,3,4,5]

print({k:v for k,v in zip(keys,values)})

