n = int(input("Enter the rows of triangle : "))
for i in range(1,n+1) :
    print(" "*(i-1),end='')
    for j in range(1,n-i+2) :
        print(j,end='')
    print()