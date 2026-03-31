a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
c = int(input("Enter the third number : "))

d = a if(a>b and a>c) else (b if(b>c) else c)
print(d,"is greatest")