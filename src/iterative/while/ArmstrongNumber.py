# Armstrong number : If sum of digits to the power number of terms is equal to the number itself then it is called as an Armstrong number.
n = int(input("Enter a positive integer : "))
count = 0
orig = n
while n!=0 :
    n//=10
    count +=1

n = orig
sum = 0
while n!= 0 :
    ld = n% 10
    sum += ld**count
    n//=10

if sum == orig :
    print(orig,"is an Armstrong number.")
else :
    print(orig,"is not an Armstrong number.")
    
