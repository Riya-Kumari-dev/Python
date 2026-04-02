a = int(input("Enter the base : "))
b = int(input("Enter the exponent : "))
pow = 1
for i in range(1,b+1) :
    pow *= a

print(a,"raised to the power",b,"is",pow)