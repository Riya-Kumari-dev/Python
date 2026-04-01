a = 10
b = 15
print(id(a))
print(id(b))
print(a is b) # id(a) == id(b) if both a and b are pointing to the same object it returns true otherwise false

a = 10
b = 10
print(id(a))
print(id(b))
print(a is b) # same as python follows reusability one object is present having value 10 both a and b are pointing to it

a = "Riya"
b = "Riya"
print(a is b)

l1 = [2,7,"Eina",34.3]
l2 = [2,7,"Eina",34.3]
print(l1 is l2) # False => lists are mutable
print(l1 == l2) # True => it is checking the content