class Employee:
    company="ABC"

    def breathe(self):
        print("I can breathe..")

    def greet(self):
        print("WELCOME")


class Programmer(Employee):
    language = "Python"

    # def breathe(self):
    #     print("Hardly have time to breathe...")
    
p1=Programmer()
p1.breathe()
p1.greet()