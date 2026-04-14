class Node :
    def __init__(self,data) :
        self.data = data
        self.next = None
class Stack :
    def __init__(self) :
        self.__head = None
        self.size = 0
    def push(self,val) :
        t = Node(val)
        t.next = self.__head
        self.__head = t
        self.size += 1
    def pop(self) :
        if self.size == 0 :
            print("Stack Undeflow")
            return -1
        val = self.__head.data
        self.__head = self.__head.next
        self.size -= 1
        return val
    def top(self) :
        if self.size == 0 :
            print("Stack Undeflow")
            return -1
        return self.__head.data
    def isEmpty(self) :
        return self.size == 0

    def display(self) :
        temp = self.__head
        while temp is not None :
            print(temp.data,end=" ")
            temp = temp.next
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
print(s.isEmpty())