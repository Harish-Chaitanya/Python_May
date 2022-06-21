


class Employee:
    company="ABC"

    def change(self,val):
        self.__class__.company=val

    @classmethod
    def class_change(cls,val):
        cls.company=val


e1=Employee()
# e1.company="XYZ"

Employee.class_change("ASD")

# e1.change("PQR")
print(e1.company)



e2 = Employee()
print(e2.company)