'''
OOPS -> Object Oriented Programming System

class -> it is like a blueprint . Theoritical concept
object -> It is real world entity.

noun  -> object
adjective -> attribute
verb ->  method

attributes(properties) -> variable
methods -> functions

4 pillars of OOPS
-abstraction -> Hiding unnecessary details
-encapsulation -> Combines attributes and methods together in one entity
-inheritance -> super class (parent) ---> derived class (child)
-polymorphism -> poly (many) + morph (forms)

'''


class Employee:
    # class attributes
    company = "ABC"

    def show(self):
        print(f"company name is : {self.company}")
    
    def greet(self):
        print("Good morning")


# creating object
obj = Employee()
obj.show()
# show(obj)

obj2 = Employee()
# instance attribute
# obj2.company = "XYZ"
obj2.show()

obj.show()