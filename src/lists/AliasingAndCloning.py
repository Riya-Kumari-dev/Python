# aliasing 
# using '=' operator
# both x and y refers to the same object change in x/y reflect in both
x = ["Nitya",65,87,"Riya"]
y = x # aliasing 
print(id(x)) 
print(id(y)) # same address as that of x
x[1] = 67
print(x) # ['Nitya', 67, 87, 'Riya']
print(y) # ['Nitya', 67, 87, 'Riya']


# cloning
# can be achieved using copy() and slicing
# different objects are created in memory 
# so changes in a will not reflect in b
a = [65,43,62,9,56]
b = a[:] # slicing
print(id(a))
print(id(b)) # diff address
a[0] = 87
print(a) # [87, 43, 62, 9, 56]
print(b) # [65, 43, 62, 9, 56]
 
a = [65,43,62,9,56]
b = a.copy() # copying
print(id(a))
print(id(b)) # diff address as that of a
a[0] = 87
print(a) # [87, 43, 62, 9, 56]
print(b) # [65, 43, 62, 9, 56]