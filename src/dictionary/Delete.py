d = {1:"Riya",3:"Nitya"}
del(d)
# print(d) # error d is not present in memory

d = {1:"Riya",3:"Nitya"}
d.clear()
print(d) # {}

d = {1:"Riya",2:"Nitya",3:"Shreya",4:"Aditi"}
del d[2]
print(d) # {1: 'Riya', 3: 'Shreya', 4: 'Aditi'}
# del d[100] # error

# pop
print(d.pop(1)) # remove 1:"Riya" and it also returns
print(d) # {3: 'Shreya', 4: 'Aditi'}
# d.pop(100) # error

print(d.popitem()) # remove any specific item
print(d)