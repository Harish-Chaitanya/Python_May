class Number:
    def __init__(self,n):
        self.num=n

    def __add__(self , other):
        return self.num + other.num
    
    def __str__(self):
        return "It is an object of class Number"

    def __gt__(self,other):
        return self.num > other.num
    
    def __len__(self):
        return self.num

obj1= Number(4)
obj2= Number(5)

# print(obj1 + obj2)
# print(obj1)
# print(obj1>obj2)
# print(len(obj1))