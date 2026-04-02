# Strong no. => a number n is said to be strong if the sum of factorial of digits in the number is equal to the number itself
n = int(input("Enter a positive number : "))
sum = 0 
orig = n
while n!=0 :
    ld = n%10
    fact = 1
    for i in range (1,ld+1) : 
        fact *= i
    sum += fact
    n//=10

if sum == orig :
    print(orig,"is a strong number.")
else :
    print(orig,"is not a strong number.")