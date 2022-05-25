'''
only if
if-else pair
if elif ladder
'''
# TODO: only if
# age = int(input("Enter your age : "))

# if age>=18:
#     print("You can drive")

# TODO : if -else pair
# age = int(input("Enter your age : "))

# if age>=18:
#     print("You can drive")
# else:
#     print("You cannot drive")

# TODO: if-elif ladder
# num = int(input("Enter a number : "))

# if num > 0:
#     print(num, " is positive")
# elif num < 0:
#     print(num , " is negative")
# else:
#     print("It is zero")


# TODO : Feedback system (1-5)
# TODO: grading system 


# TODO: Nested if else
'''
if: 
    if:
        //if statements
else:
    if:
        //if statements
    else:
        //else statements

'''

num1 = 5
num2=8
num3=12

if num1 > num2:
    if num1 > num3 : 
        print("Num1 is greatest")
    else:
        print("Num3 is greatest")
else:
    if num2>num3:
        print("Num2 is greatest")
    else:
        print("Num3 is greatest")


'''
# whether user is signed in or not
is_google =True
is_facebook=False
is_email = True
'''
is_google =True
is_facebook=False
is_email = True

# if (is_google or is_facebook or is_email):
#     print("You are signed in")
# else:
#     print("Please sign in")

# if is_google:
#     print("You are signed in")
# elif is_email:
#     print("You are signed in")
# elif is_facebook:
#     print("You are signed in")
# else:
#     print("Please signed in")


# if is_google:
#     print("Signed in")
# else:
#     if is_facebook:
#         print("Signed in")
#     else:
#         if is_email:
#             print("signed in")
#         else:
#             print("Please sign in")


'''
is_cart= True
is_pay = True
is_loggedin = True
# Whether user can make purchase or not
'''

is_cart= False
is_pay = True
is_loggedin = True

# if (is_cart and is_pay and is_loggedin):
#     print("order placed successfully")
# else:
#     print("Cannot place order")

if is_loggedin:
    if is_cart:
        if is_pay:
            print("Order placed successfully")
        else:
            print("cannot place order")
    else:
        print("cannot place order")
else:
    print("cannot place order")



