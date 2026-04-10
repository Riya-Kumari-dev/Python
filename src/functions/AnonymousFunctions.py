# Anonymous Functions
# lambda argument : expression
# if we want to use the function only once

a = lambda x : x*x*x # cube 
print(a(10)) 

f = lambda x,y : x+y
print(f(10,20))

# filter 
# filter on the basis of expression
f = filter(lambda x : x%3==0,[10,20,30,40,23,63])
output = list(f)
print(output) # [30,63]

# map
# same number of elements
m = list(map(lambda x : x*x*x,[1,2,4,6]))
print(m)  # [1, 8, 64, 216]

a  = [1,2,8,5]
b = [10,23,54,65]
m2 = list(map(lambda x,y : x+y, a,b))
print(m2)