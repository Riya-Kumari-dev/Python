class BTNode :
    def __init__(self,data) :
        self.data = data
        self.left = None
        self.right = None

def height(root) :
    if root is None :
        return 0
    return 1 + max(height(root.left) ,height(root.right))

def isBalanced(root) :
    if root is None :
        return True
    if (height(root.left) - height(root.right)) not in [-1,0,1] :
        return False
    return isBalanced(root.left) and isBalanced(root.right) 

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

print(isBalanced(a))