# Logical operators work on everything
# not => return opposite 
flag = True
print(not flag) # False 
print(not (4>5)) # True
print(not 10) # False
print(not "Riya") # False

# and => both value true
# if first one is false return first one
# if first one is true return second one
a = 5
b = 2
print((a>b) and (a>=b)) # True
print("Riya" and 10) # "Riya" is true => 10
print(0 and 3+4j) # 0 => false => 3+4j

# or => return if anyone is true
# first is false return second one
# first is true return first one

print((a>b) or (a<b)) # True
print("Gupta" or 34.2) # Gupta
print(0.0 or 3+5j) # 3 + 5j
print("" or 23) # 23