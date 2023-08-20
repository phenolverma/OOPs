class A:
    def whoami(self):
        print('Im in A')


class B(A):
    def whoami(self):
        print('Im in B')


class C(A):
    def whoami(self):
        print('Im in C')


class D(B, C):
    pass


d1 = D()
d1.whoami()
# Method Resolution Order
