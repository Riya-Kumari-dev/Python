class Node :
    def __init__(self,data) :
        self.data = data
        self.next = None
class Queue :
    def __init__(self) :
        self.__head = None
        self.__tail = None
        self.size = 0
    def enqueue(self,val) :
        t = Node(val) 
        if self.size == 0 :
            self.__head = self.__tail = t
        else :
            self.__tail.next = t
            self.__tail = t
        self.size+=1
    def dequeue(self) :
        if self.size == 0 :
            print("Underflow")
            return
        self.__head = self.__head.next
        self.size -= 1
    def front(self) :
        if self.size == 0 :
            print("Underflow")
            return -1
        return self.__head.data
    def isEmpty(self) :
        return self.size == 0
    def display(self) :
        temp = self.__head
        while temp is not None :
            print(temp.data,end = " ")
            temp = temp.next
        print()

q = Queue()
q.dequeue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.display()
print(q.front())
print(q.isEmpty())
q.dequeue()
q.display()