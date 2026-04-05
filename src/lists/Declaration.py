# lists
# - Duplicate allowed 
# - Order preserve
# - Slicing
# - Indexing
# - Mutable 
# - Heterogeneous

l = [4,3,"Riya",5] 
print(l)
l2 = [] 
for i in range(1,6) :
    l2.append(i)
print(l2)

l3 = list(range(1,6))
print(l3)
l4 = eval(input("Enter a list : "))
print(type(l4))
print(l4)

l4 = [0 for i in range(6)] # store 0 6 times in l4
print(l4)
l4 = [i for i in range(5)] # 0 1 2 3 4
print(l4)