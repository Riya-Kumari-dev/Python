class BTNode :
    def __init__(self,data) :
        self.data = data
        self.left = None
        self.right = None
def isSumProperty(root):
        # code here
    if root is None or (root.left == None and root.right == None):
        return True
    if root.left :
        ldata = root.left.data
    else :
        ldata = 0
    if root.right :
        rdata = root.right.data
    else :
        rdata = 0
    if (root.data == ldata + rdata) and isSumProperty(root.left) and isSumProperty(root.right) :
        return True
    else :
        return False


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

print(isSumProperty(a))