class Stack:
    def __init__(self,size):
        self.stack = list()
        self.maxSize = size
        self.top = 0
    def push(self,data):
        if self.top>=self.maxSize:
            return ("Stack Full!")
        self.stack.append(data)
        self.top += 1
        return True
    def pop(self):
        if self.top <= 0:
            return ("Stack Empty!")
        item = self.stack.pop()
        self.top -= 1
        return item
    def size(self):
        return self.top

if __name__=='__main__':
    s1=Stack(10)
    s1.push(99)
    s1.push(88)
    s1.push(77)
    print('Before Pop',s1.__dict__)
    s1.pop()
    print('After Pop', s1.__dict__)
    s1.push(8888)
    print('After Pop', s1.__dict__)
