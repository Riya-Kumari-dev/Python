import math
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

def countNodes(root) :
    if root is None :
        return 0
    return 1 + countNodes(root.left) + countNodes(root.right)

def height(root) :
    if root is None :
        return 0
    return 1 + max(height(root.left) ,height(root.right))

def sum(root) :
    if root is None :
        return 0
    return root.data + sum(root.left) + sum(root.right)

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
print(height(a))
print(countNodes(a))
print(sum(a))