class Node :
    def __init__(self,data) :
        self.data = data
        self.next = None

print("Enter a list of values : ",end="")
l = [int(ele) for ele in input().split()] # user input of a list

# now make the linked list
head = None
temp = None
for i in range(len(l)) :
    t = Node(l[i])
    if head is None :
        head = t
        temp = head
    else :
        temp.next = t
        temp = t

# counting
count = 0
temp = head
while temp is not None :
    count += 1
    temp = temp.next
print("Total number of nodes present is",count)