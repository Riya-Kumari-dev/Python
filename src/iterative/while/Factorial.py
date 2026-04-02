n = int(input("Enter a positive number : "))
fact = 1
i=1
while i<=n: 
    fact *= i
    i = i+1

print("Factorial of",n,"is",fact)