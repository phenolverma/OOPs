class Employee:
    empCount = 0
    def __init__(self, getname, getsalary):
        self.name = getname
        self.salary = getsalary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee: ", Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, "\nSalary: ", self.salary)

e1=Employee('Gaurav',45000)
print( e1.__dict__)
print(Employee.__name__)
print(e1.__doc__)
print(e1.__module__)
