class Queue :
    def __init__(self) :
        self.__l = []
        self.rear = -1
        self.f = 0
        self.size = 0
    def enqueue(self,val) :
        self.__l.append(val)
        self.rear += 1
        self.size += 1
    def dequeue(self) :
        if self.size == 0 :
            print("Underflow")
            return
        self.f += 1
        self.size -= 1
    def front(self) :
        if self.size == 0 :
            print("Underflow")
            return -1
        return self.__l[self.f]
    def isEmpty(self) :
        return self.size == 0
    def display(self) :
        for i in range(self.f,self.rear+1) : 
            print(self.__l[i],end=" ")
        print()
    
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
print(q.front())
q.dequeue()
q.display()
print(q.isEmpty())