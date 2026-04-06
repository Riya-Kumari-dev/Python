# add, remove, insert => no such methods on tuple because it is immutable

a = (2,5,1)
# len
print(len(a)) # 3

a = ((2,4),"Tiya")
print(len(a)) # 2

# count() => count number of occ of ele in tuple
print(a.count(1)) # 0

# sorted
a = (12,45,2,0,8)
b = sorted(a) # generalized method
print(a) #  (12, 45, 2, 0, 8) # a is same
print(b) # [0, 2, 8, 12, 45] # with sorted a list is return

# a = (1,2,3,"Riya",-1)
# b = sorted(a) # error '<' not supported between instances of 'str' and 'int'
# print(b)

# min , max 
print(min(a)) # 0
print(max(a)) # 45

# comprehension does not work for tuple