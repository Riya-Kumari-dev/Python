class Stack :
    def __init__(self) :
        self.__l = []
        self.size = 0
    def push(self,val) :
        self.__l.append(val)
        self.size += 1
    def pop(self) :
        if self.size == 0 :
            print("Empty Stack")
            return -1
        ele = self.__l.pop()
        self.size -= 1
        return ele
    def isEmpty(self) :
        return size == 0
    def top(self) :
        if self.size == 0 :
            print("Empty Stack")
            return -1
        return self.__l[len(self.__l)-1]
    def display(self) :
        for i in range(self.size) :
            print(self.__l[i],end=" ")
        print()

s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.pop()
s.display()
print(s.pop())
s.push(40)
s.push(50)
print(s.top())
print(s.size)
s.display()