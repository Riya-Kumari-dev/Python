n = int(input("Enter a positive integer : "))
l = [] # empty list
for i in range(1,n+1) :
    if n% i == 0 :
        l.append(i)

print(l)