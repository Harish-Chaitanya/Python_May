'''
we execute while loop when we do not know no of iterations
'''

# TODO: WAP to count no of digits
# 72283  -> 5
# 123 ->3 
# 675

# num = int(input("Enter a number: "))

# count = 0 

# while num>0:
#     rem = num%10
#     print("rem: ",rem)
#     count = count+1
#     num=num//10

# print("No of digits: ",count)


# WAP to reverse given digit
# 345 -> 543
# 8651 -> 1568

# num=int(input("Enter a num: "))
# rev=0
# while num > 0:
#     rem=num%10
#     rev= (rev*10)+rem
#     num=num//10

# print("Reverse of given digit is: ",rev)
# WAP to find whether a given number is pallindrome or not
# 121 -> 121 (it is a pallindrome)
# 123 ->321 (not a pallindrome)

num =int(input("Enter a number: "))

rev=0
temp = num
while num > 0:
    rem=num%10
    rev=(rev*10)+rem
    num=num//10
print("Reverse num is: ",rev)

if rev == temp:
    print("It is a pallindrome number")
else:
    print("It is not a pallindrome number")


