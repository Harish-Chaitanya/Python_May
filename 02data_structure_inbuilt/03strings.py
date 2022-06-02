'''
strings -> '' , " " , ''' ''' , """ """
immutable
ordered
iterable
'''

s= "we are learning python"
# print(len(s))
# print(s[1])
# print(s[2])

# print(s[4:])
# print(s[: 5:])

# print(s[ : : -1])

# print(s.capitalize())
# print(s.title())
# print(s.upper())
# print(s.lower())

# print(s.find("sre"))
# print(s.find("are"))

# print(s.index("are"))
# print(s.index("sre"))

# print(s.count('e'))


# print(s.startswith("we"))
# print(s.endswith("we"))

# s= "weareleWarningpython"

# print(s.isalnum())
# password = "          "
# print(password.isspace())

# contact = "123"

# print(contact.isdigit())

# print(s.islower())


# TODO: replace 
s= "we are learning python"
# print(s.replace('a','@',1))
# print(s.replace(' ','',2))


# TODO: strip -> to remove extra spaces

password = "             ab c123          "
# print(password)
# print(password.lstrip())
# print(password.rstrip())
# print(password.strip())

# TODO: split
s= "we are learning python"
# print(s.split())
# print(s.split("e",2))


# TODO: join

# fname="john"
# lname="doe"
# uname=".".join([fname,lname])
# # print(uname)
# domain="abc.com"
# email='@'.join([uname,domain])
# # print(email)

# print(email.split('@'))

# TODO: escape sequences
'''
\n -> new line
\t -> tab
\b -> backspace
\a -> alert
\\ ->\
\'->'
'''
# path = r"C:\new\temp\docs"
# print(path)

# TODO: printing formats
n1=5
n2=3
ans=n1+n2

# n1 + n2 = ans

# print(str(n1) + '+' + str(n2) + '=' + str(ans))

# print("{0} + {1} = {2} ".format(n1,n2,ans))

# TODO: f-strings
# print(f"{n1} + {n2} = {ans}")

