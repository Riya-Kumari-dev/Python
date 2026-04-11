def f(a, b) :
    '''This function returns sum and difference of two parameters'''
    return a+b, a-b

sum,diff = f(10,20) 
print(sum) # 30
print(diff) # -10
print(type(f(1,2))) # tuple
print(f.__doc__)  # object.__doc__ => return doc string => This function returns sum and difference of two parameters