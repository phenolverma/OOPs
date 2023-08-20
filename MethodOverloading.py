class Student:
    def hello(self, name=None,roll=123):
        if name is not None:
            print('Hey ' ,name,roll )
        else:
            print('Hey ')
std = Student()
std.hello()
std.hello('Nicholas')
std.hello('Amit',567)


