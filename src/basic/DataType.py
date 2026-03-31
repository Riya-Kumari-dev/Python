# String
name1 = "Riya Gupta"
name2 = 'Riya Gupta'
name3 = '''Riya Gupta'''

print("Variable :",name1,"  Data Type :",type(name1)) # <class 'str'> => String type 
print("Variable :",name2,"  Data Type :",type(name2))
print("Variable :",name3,"  Data Type :",type(name3))

# int

age = 24
climate = -2

print("Variable :",age,"    Data Type :",type(age)) # <class 'int'> => int type
print("Variable :",climate,"    Data Type :",type(climate))


# float
price = 367.65
print("Variable :",price,"  Data Type :",type(price)) # <class 'float'>

# boolean
# True False first letter capital
flag = True
isSafe = False

print("Variable :",flag,"   Data Type :",type(flag)) # <class 'bool'>
print("Variable :",isSafe," Data Type :",type(isSafe))

# None 
# No value

val = None
print("Variable :",val,"    Data Type :",type(val)) #<class 'NoneType'>


# binary form
# can be start with 0b / 0B 
a = 0b1000 # only 1000 will convert to decimal
b = 0B1000
print(a,b) # printing will be in decimal only

# 1.2 * 10^3 
c = 1.2e3 # e is for 10^
d = 1.2E3
print(c)
print(d) # both are same

# e = 0b1.1e3 # invalid
