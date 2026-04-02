# n is called as a perfect number if the sum of all the factors of n excluding itself is equal to n
n = int(input("Enter a positive number : "))
sum = 0
for i in range(1,n) : # to exclude n
    if n%i == 0 :
        sum += i

if sum == n :
     print(n,"is a perfect number.")
else :
    print(n,"is not a perfect number.")