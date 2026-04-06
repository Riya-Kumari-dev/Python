# set
# Duplicates are not allowed 
# Unordered but we can sort
# No indexing
# No String concept
# Heterogeneous
# Mutable

# empty set
s = set()
print(s) # set()
print(type(s)) # <class 'set'>

s = {2,31,8}
print(type(s)) # <class 'set'>
s = set("RiyaGupta")
print(s) # {'y', 'p', 'u', 'G', 'i', 'a', 't', 'R'}
a = set(range(1,10))
print(a) # {1, 2, 3, 4, 5, 6, 7, 8, 9}

# add
b = set() 
b.add(1)
b.add("Riya")
print(b) # {1, 'Riya'}
b.add((2,3,1))
print(b)  # {(2, 3, 1), 1, 'Riya'}
# b.add({1,2}) # error
# b.add([4,3,1]) # error  cannot use 'list' or any other sequence apart from string and tuple as a set element (unhashable type: 'list')

# update
# to add sequence
# works on iterable elements
b.update([32,1])
b.update({3,2})
print(b) # {'Riya', 1, 32, 2, 3, (2, 3, 1)}

# copy
b = {1,2,1,3}
a = b.copy()
print(a) # {1, 2,3}
print(b) # {1, 2, 3}

# pop 
print(a.pop()) # return and remove any element

# remove 
# remove particular element if present cannot return anything
# a.remove(4) # error
a.remove(2)
print(a) # {3}

a.clear() 
print(a) # set()
a = {4,3,1,6,5}
print(a.discard(5)) # None
print(a) # {1, 3, 4, 6}
a.discard(50) # No error but does nothing

# union
b = {4,3,2}
print(a.union(b)) # {1, 2, 3, 4, 6}
print(b.union(a)) # {1, 2, 3, 4, 6}
print(a|b) # {1, 2, 3, 4, 6}
# a and b remains same only it returns  a union b but no change in a or b

# intersection
print(a.intersection(b))  # {3, 4}
print(a&b) # {3, 4}

# set difference
print(a.difference(b)) # a - b => ele present in a not b => {1, 6} 
print(b-a)  # {2} => ele present in b not a 

# symmetric difference
print(a.symmetric_difference(b)) # a-b union b-a =>  {1,2,6}
print(a^b) # {1,2, 6}