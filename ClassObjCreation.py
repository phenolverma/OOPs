class Employee:
    empCount = 0
    empNation = 'India'

    def __init__(self, getname, getsalary=20000):
        self.name = getname
        self.salary = getsalary
        Employee.empCount += 1

    def displayEmployee(self):  # Object Method
        print("Name : ", self.name, "\nSalary: ", self.salary)
        print('Country:', self.empNation)

    @classmethod  # U were not able to call method by class
    def displayCount(self):  # class method
        print("Total Employee: ", self.empCount)
        print("Nation: ", self.empNation)

    @staticmethod  # u were not able to call a method by object
    def addNumbers(x, y):
        return x + y


if __name__ == "__main__":
    e1 = Employee('Gaurav', 45000)
    print(e1.__dict__)
    e2 = Employee('Aditya')
    e2.displayEmployee()
    e2.displayCount()
    print('%%%%%%%%%%%%%')
    Employee.displayCount()
    print(e2.addNumbers(89, 11))
# Only and Only objects can call the methods not the classes
# Your Expectation : i wish to call this function with class only
# Decorator --> function which gives extension to another function
# Extension--> Object --> Class
