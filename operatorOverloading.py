class A:
    def __init__(self, geta):
        self.a = geta

    def __add__(self, other):
        return self.a * other.a


ob1 = A(10)
ob2 = A(78)
print(ob1 + ob2)  # ob1.__add__(ob2)

# Operator Overloading is implemented with the help of method overriding
