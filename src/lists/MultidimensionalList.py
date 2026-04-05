l = [1,2,[7,"Riya"]]
print(l) 

# multidimensional
l = [[1,2,3,4],[76,43,8],[5,9,12,0]]
print(l)
print(l[1]) # [76,43,8]
print(l[0][1]) # 2
print(len(l)) # 3
print(len(l[0])) # 4

l = [[j for j in range(4)] for i in range(5)]  # [[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]]
print(l)
# taking input
dim = input("Enter the dimensions for a 2d list : ").split()
m = int(dim[0])
n = int(dim[1])
l = []
for i in range(m) :
    row = [int(ele) for ele in input().split()]
    l.append(row)

print(l)

dim = input("Enter the dimensions for a 2d list : ").split()
m = int(dim[0])
n = int(dim[1])
print("Enter",m*n,"elements for the list : ")
lis = [int(ele) for ele in input().split()] # 1d list
l = []
for i in range(m) : 
    begin = n*i
    end = n*(i+1)
    row = lis[begin : end]
    l.append(row)

print(l)