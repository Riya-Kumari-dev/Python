# Tuple : 
# same as list but immutable
# Ordered
# Indexing
# Slicing
# Heterogeneous
# Duplicate allowed
# (1,2,3)
# if we are giving a variable more than two elements it is by default tuple

a = (1,2,3) # <class 'tuple'>
print(type(a))
b = 3,4,5 # Paranthesis is optional as we are assigning multiple values to a variable by default it becomes a tuple
print(type(b)) # <class 'tuple'>
c = ()
print(type(c)) # <class 'tuple'>

# with single element we cannot create a tuple 
a = (10+20)*30 
print(a) # 900
print(type(a)) # <class 'int'>
b = (10+20)*(30)
print(b) # 900
print(type(b))  # <class 'int'>

# if we want a single element as tuple
t = (1,)
print(type(t)) # <class 'tuple'>

# Just like string and list => tuple also have + as concatenation and * as repetition operator
a = (1,2,3)
b = (4,5,6)
c = a+b # concatenation
print(c)
d = a*3 # repetition operator
print(d)

# Immutable
# a[0] = 3 # 'tuple' object does not support item assignment
# print(a)

# slicing
print(a[1:])