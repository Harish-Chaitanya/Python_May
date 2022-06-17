class Employee:
    # class attributes
    company = "ABC"

    def show(self):
        print(f"company name is : {self.company}")
    
    @staticmethod
    def greet():
        print("Good morning")


# creating object
obj1 = Employee()
obj2 = Employee()


obj1.greet()
obj2.greet()