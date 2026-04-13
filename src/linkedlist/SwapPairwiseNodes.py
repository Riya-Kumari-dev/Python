class Node :
    def __init__(self,data) :
        self.data = data
        self.next = None

def pairWiseSwap(head):
        # code here
    dummy = Node(0)
    prev = dummy
    curr = None
    Next = None
    dummy.next = head
    while prev.next and prev.next.next :
        curr = prev.next
        Next = curr.next
        # swap
        curr.next = Next.next
        Next.next = curr
        prev.next = Next
            
        prev = curr
    return dummy.next  

a = Node(1)
b = Node(3) 
c = Node(4)
d = Node(7)
e =  Node(9)
f = Node(10) 
g = Node(1)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g

head = a
head = pairWiseSwap(head)
# display
temp = head
while temp is not None :
    print(temp.data,end="-->")
    temp = temp.next
print("None")