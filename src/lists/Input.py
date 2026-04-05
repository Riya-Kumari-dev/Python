# taking a space seperated sequence of integers from user
s = input("Enter a list : ").split() 
l = []
for ele in s :
    l.append(int(ele))

print(l)

# first input no of elements and then elements by space
n = int(input("Enter the number of elements for the list : "))
s = input("Enter elements for the list : ").split()
l2 = [] 
for ele in s :
    l2.append(int(ele))

print(l2)

# first input no. of elements and then elements by entering
n = int(input("Enter the number of elements for the list : "))
l3 = [] 
print("Enter",n,"elements for the list : ")
for i in range(n) :
    l3.append(int(input()))

print(l3)