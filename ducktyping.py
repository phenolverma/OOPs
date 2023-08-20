class Pycharm:
	def execute(self):
		print('Compiling')
		print('Running')
class Mycharm:
    def execute(self):
        print('SpellCheck')
        print ('Compiling')
        print ('Running')
class Laptop:
	def code(self,a):
		a.execute()
l1=Laptop()
p1=Pycharm()
m1=Mycharm()
l1.code(p1)
