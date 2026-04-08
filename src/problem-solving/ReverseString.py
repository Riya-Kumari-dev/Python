s = "Riya"
print(s[::-1])

l = list(s)
n = len(l)
for i in range(0,n//2) :
    temp = l[i]
    l[i] = l[n-i-1]
    l[n-i-1] = temp

s = ''.join(l)
print(s)