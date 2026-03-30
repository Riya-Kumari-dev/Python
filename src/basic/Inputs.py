# All the inputs by default are string
name = input("Enter your name : ")
print("Welcome",name,type(name))

age = input("Enter your age : ")
print("Age : ", age, type(age))

# for that we have to cast the inputs into whichever type we want
b = int(input("Enter your age : "))
print("Age : ", b, type(b))