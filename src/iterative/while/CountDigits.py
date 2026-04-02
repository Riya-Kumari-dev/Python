n = int(input("Enter a positive number : "))
count = 0
orig = n
while n!=0 :
    n//=10
    count +=1

print("The number of digits in",orig,"is",count)