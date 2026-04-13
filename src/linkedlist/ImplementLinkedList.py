class Node :
    def __init__(self,data) :
        self.data = data
        self.next = None
class LinkedList :
    # initializing the linked list with list as input
    def __init__(self,l=[]) :
        self.head = None
        self.size = 0
        temp = None
        for i in range(len(l)) :
            t = Node(l[i])
            if self.head is None :
                self.head = t
                temp = self.head
            else :
                temp.next = t
                temp = t
            self.size += 1

    # display 
    def display(self) :
        temp = self.head
        while temp is not None :
            print(temp.data,end="-->")
            temp = temp.next
        print("None")

    # insertion
    def insert(self,val,idx) :
        t = Node(val) 
        if idx < 0 or idx > self.size :
            print("Index Error")
            return 
        # at the beginning
        if idx == 0 :
            t.next = self.head
            self.head = t
        else :
            temp = self.head
            for i in range(idx-1) : 
                temp = temp.next
            t.next = temp.next
            temp.next = t
        self.size += 1

    # removal 
    def remove(self,idx) : 
        if idx < 0 or idx >= self.size :
            print("Index Error")
            return 
        if self.head == None :
            print("Underflow Error")
            return
        if idx == 0 :
            self.head = self.head.next
        else :
            temp = self.head
            for i in range(idx-1) : 
                temp = temp.next
            temp.next = temp.next.next
        self.size -= 1
        
        

l = LinkedList([10,20,50])
l.display()
l.insert(30,2)
l.insert(60,3)
l.display()
l.insert(70,5)
l.insert(100,0)
l.display()

l.remove(2)
l.display()
l.remove(0)
l.remove(4)
l.display()