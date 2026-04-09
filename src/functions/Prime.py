import math
def prime(n) :
    if n == 1 :
        return False
    for i in range(2,int(math.sqrt(n))+1) : 
        if n%i == 0 :
            return False
    return True

print("Prime Numbers between 1 and 60 : ",end=" ")
for i in range(1,60) :
    if prime(i) == True :
        print(i,end=" ")