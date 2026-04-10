# Positional Argument
def f(a,b,c) :
    return a+b-c

print(f(10,20,30)) # 0
print(f(30,20,10)) # 40
# here it is positional argument as if we are changing the position the values also changes

# Keyword Argument
def f2(name, age, id) :
    print(name) # Riya
    print(age) # 22
    print(id) # 1

f2(age = 22, name = "Riya",id = 1) 
# This is keyword argument
# Any order is possible now with keyword as argument name

# f2(name = "Sneha",2,20) # error # positional argument follows keyword argument
f2("Sneha",id = 2,age = 22) # ✅

# Default Arguments 
def sum(a,b,c=0) : # c is taking as default value. If we don't pass c then 0 is taken
    return a+b+c

print(sum(20,30)) # a=20,b=30 , we didn't pass c value => default c=0 => 20+30+0 => 50
print(sum(20,30,50)) # a=20, b=30, c=50 => 100

# def sum(a=0,b,c) : # error # Non default argument follows default argument
#     return a+b+c

# print(sum(10,20))

# Any number of argument
def add(*n) : # varied number of arguments
    sum = 0
    for ele in n :
        sum += ele
    return sum

print(add(1,2,3,4)) # 10
print(add(1,2)) # 3
print(add(0)) # 0

# Variable length argument
def f(*n) :
    for ele in n :
        print(ele)

f(1,2,"Riya")

def f2(*a,x,y) : # x and y must be keyword argument
    for ele in a :
        print(ele)
    print(x)
    print(y)

# f2(10,20,30,40) # error
f2(10,20,"Riya",y=40,x=20) # ✅

# variable length keyword argument
def f(**a) : # dictionary => {a:10,c:30,d:"Riya",b:40,e:20}
    for key,value in a.items() :
        print("Key :",key,"Value :",value) 

f(a=10,c=30,d="Riya",b=40,e=20) 
# Key : a Value : 10
# Key : c Value : 30
# Key : d Value : Riya
# Key : b Value : 40
# Key : e Value : 20