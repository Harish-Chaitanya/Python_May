from tkinter import N


class Employee:
    company = "ABC"

    def __init__(self,n,a):
        self.name = n
        self.age = a

    
    def profile(self):
        print(f"Name is {self.name} and age is : {self.age}")

e1=Employee("John",23)

e2=Employee("Jane",25)

e1.profile()
e2.profile()