class BTNode :
    def __init__(self,data) :
        self.data = data
        self.left = None
        self.right = None
    
def preOrder(root) :
    if root is None:
        return
    print(root.data,end = " ")
    preOrder(root.left)
    preOrder(root.right)

def inOrder(root) :
    if root is None:
        return
    inOrder(root.left)
    print(root.data,end = " ")
    inOrder(root.right)

def postOrder(root) :
    if root is None:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.data,end = " ")

a = BTNode(10)
b = BTNode(20)
c = BTNode(30)
d = BTNode(40)
e = BTNode(50)
f = BTNode(-10)
g = BTNode(60)
h = BTNode(50)
i = BTNode(90)

a.left = b
a.right = c

b.left = d
b.right = e

c.left = f
c.right = g

d.left = h
e.right = i

preOrder(a)
print()
inOrder(a)
print()
postOrder(a)