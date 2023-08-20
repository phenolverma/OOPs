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
e2=Employee('jatin',45000)
e1.displayEmployee()
e2.displayEmployee()
print(getattr(e1,'name'))#e1.name,e1.salary
setattr(e1,'name','Virat')#e1.name='Virat'
print(getattr(e1,'name'))# returning e1.name
print(e1.__dict__)
print(hasattr(e1,'salary'))
print(e2.empCount)


