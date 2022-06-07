'''
files are used to store simpler data

text file -> .py ,.txt , .doc , .html
binary file -> .png , .jpg , .pdf , .mp3

text file modes
r -> read mode
w -> write mode
a -> append mode

binary file modes
rb -> read mode
wb -> write mode
'''


# file = open("../01basics/00hello.py",'r')

# data= file.read(6)
# data= file.readlines()
# print(data[0])

# print(file.readline())
# print(file.readline())

# file.seek(10)
# print(file.read())
# file.close()


# TODO: writing a file
# file = open("./test.txt" , 'w')
# print("suceess")
# file.write("Writing using python program")
# file.write("Good morning")
# file.close()

# TODO: append mode

# file = open("./test.txt",'a')
# file.write(" appending the content")
# file.close()


# TODO: copying file

# with open("./01functions.py" , 'r')  as f1 , open("./copy.txt",'w') as f2:
#     data = f1.read()
#     f2.write(data)


with open("./pic.jfif",'rb') as f1 , open("copy.jfif","wb") as f2:
    data=f1.read()
    f2.write(data)

