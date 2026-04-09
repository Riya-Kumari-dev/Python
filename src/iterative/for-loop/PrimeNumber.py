import math
n = int(input("Enter a positive integer : "))
prime = True
for i in range(2,int(math.sqrt(n))+1) : 
    if n%i == 0 :
        prime = False
        break

if prime == True :
    print(n,"is a prime number.")
else :
    print(n,"is not a prime number.")