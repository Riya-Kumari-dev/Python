def f() :
    a = 10 # local Variable its scope is limited to f()
    print(a)

f()
# print(a) # error as a is not defined

x = 2 # global variable can be access anywhere 
def f2() :
    y = 100
    print(x)
    print(t)
    print(y)

t = 20 # t is also global it's just that we must declare the variable before calling the function  in which we want to use
f2()
print(x) 