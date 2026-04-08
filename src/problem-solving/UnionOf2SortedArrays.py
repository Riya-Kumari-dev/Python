a = [1,2,5,6,7]
b = [2,5,7,8]
s1 = set(a)
s2 = set(b)
l = list(s1|s2)
print(l)

# but the above solution will show time complexity error
# the following code is only for unique elements 
i = 0
j = 0
l = []
while i<len(a) and j<len(b) :
    if a[i] < b[j] :
        l.append(a[i])
        i += 1
    elif a[i] == b[j] :
        l.append(a[i])
        i+=1
        j+=1
    else :
        l.append(b[j])
        j += 1

while i<len(a) :
    l.append(a[i])
    i+=1
while j<len(b):
    l.append(b[j])
    j+=1

print(l)