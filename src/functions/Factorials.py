def factorial(n) :
    fact = 1
    for i in range(1,n+1) :
        fact *= i
    return fact

for i in range(1,11) :
    print("Factorial of",i,"is",factorial(i))