class BTNode :
    def __init__(self,data) :
        self.data = data
        self.left = None
        self.right = None

def isIdentical(root1,root2) :
    if root1 is None and root2 is None :
        return True
    if root1 and root2 :
        return (root1.data == root2.data) and isIdentical(root1.left,root2.left) and isIdentical(root1.right,root2.right)
    else :
        return False
a = BTNode(10)
b = BTNode(20)
c = BTNode(30)
a.left = b
a.right = c

d = BTNode(10)
e = BTNode(20)
f = BTNode(30)
d.left = e
d.right = f

print(isIdentical(a,d))