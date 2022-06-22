class Employee:
    salary = 5000

    @property
    def changeSalary(self):
        return self.salary

    @changeSalary.setter
    def changeSalary(self,val):
        self.salary=val


e1=Employee()
# print(e1.changeSalary())
print(e1.changeSalary)

e1.changeSalary=9000
print(e1.changeSalary)
