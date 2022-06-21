class Human:
    eyes=2

    def breathe(self):
        print("I can breathe")

class Employee:
    company="ABC"

    def breathe(self):
        print("I do get time to breathe")
    
    def greet(self):
        print("WELCOME")

class Programmer( Human, Employee):
    language="Python"

    def __init__(self,n,a):
        self.name = n
        self.age = a
    
    # def breathe(self):
    #     print("Hardly gets time to breathe")
    

p1=Programmer("John",12)
p1.breathe()