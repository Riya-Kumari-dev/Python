class Node :
    def __init__(self,data) :
        self.data = data
        self.next = None

def display(head) :
    temp = head
    while temp is not None :
        print(temp.data,end="-->")
        temp = temp.next
    print("None")
def reverse(head):
        # code here
    prev = None
    curr = head
    Next = None
    while curr is not None:
        Next = curr.next
        curr.next = prev
        prev = curr
        curr = Next
    return prev

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
display(head)
head = reverse(head)
display(head)