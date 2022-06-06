'''
self calling function

we have a bigger problem

base case
we find solution for smaller  problem


'''

# find sum of first 5 digits
# 5+4+3+2+1

# f(n) = n + f(n-1)
# f(5) = 5 + f(4)
# f(4) = 4 + f(3)
# f(3) = 3+ f(2)
# f(2) = 2+ f(1)
# f(1) = 1 (base condition)

def func(num):
    # base condtion
    if num == 1:
        return 1
    return num + func(num-1)


# print(func(3))


# Find factorial of a number recursively
# 5! = 5*4*3*2*1

# TODO: Find power of a number recursively

# num = 3
# pow =2

def power ( num , pow):
    # base case
    if pow ==0:
        return 1
    return num * power(num , pow-1)



# TODO: Binary Search 

def binary_helper(arr , low , high , val ):
    if low > high :
        return "NO MATCH"
    
    mid = low + ((high-low)//2)

    if arr[mid] > val :
        return binary_helper(arr,low , mid -1 ,val)
    elif arr[mid] < val:
        return binary_helper(arr , mid + 1 , high , val)
    else:
        return mid

def rec_binary(arr,val):
    return binary_helper(arr , 0 , len(arr)-1 , val)

print(rec_binary([1,2,3,4,5,6,7] , 15))