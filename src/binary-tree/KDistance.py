class BTNode :
    def __init__(self,data) :
        self.data = data
        self.left = None
        self.right = None

def distance(root,k,list) :
    if root is None :
        return
    if k==0 :
        list.append(root.data)
        return
    distance(root.left,k-1,list)
    distance(root.right,k-1,list)
    

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

l = []
distance(a,2,l)
print(l)