n = int(input("Enter the rows of triangle : "))
a = 2*n-3
for i in range(1,2*n) :
    if i <= n :
        print(" "*(n-i),end='')
        print('*'*(2*i-1))
    else :
        print(" "*(i-n),end = '')
        print('*'*a)
        a-=2
    