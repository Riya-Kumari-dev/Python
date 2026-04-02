n = int(input("Enter a positive number : "))
sum = 0 
orig = n
while n!=0 :
    sum += n%10
    n//=10

print("The sum of digits in",orig,"is",sum)
