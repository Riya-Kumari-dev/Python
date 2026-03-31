a = 5
b = "4" # it is of string type
c = int(b) 
sum = a+c
print(sum)

# name = "Riya"
# c = int(name) # will show error it is not possible to convert
# sum = a+c
# print(sum)

print(int(12.3)) # 12
# print(int("12.3")) errror
# print(int(1+3j))
print(int(True)) # 1

# float()

print(float(23)) # 23.0 
print(float("34")) # 34.0
print(float("2.34")) # 2.34
print(float(False)) # 0.0
# print(float(3+2j)) error

# string()

print(str(23)) # 23
print(str(23.4)) # 23.4
print(str(False)) #False
print(str(3+6j)) # (3+6j)

# bool()
# => everything true except zero and empty string

print(bool(23)) # True
print(bool(0.0)) # False
print(bool(-21.4)) # True
print(bool(2+4j)) # True
print(bool("")) # False
print(bool("type")) # True