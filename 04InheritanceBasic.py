from ClassObjCreation import Employee


class Programmer(Employee):
    def __init__(self, getname, getsal, getproject):
        Employee.__init__(self, getname, getsal)
        self.project = getproject

    def displayEmployee(self):  # Method Overriding
        Employee.displayEmployee(self)
        print("Project:", self.project)


class Manager(Employee):
    pass


if __name__ == '__main__':
    p1 = Programmer('Jatin', 50000, 'TMO')
    m1 = Manager('Pradeep')
    p1.displayEmployee()
    print('%%%%%%%%%%%')
    m1.displayEmployee()
    Manager.displayCount()

    # print(Employee.empCount)
