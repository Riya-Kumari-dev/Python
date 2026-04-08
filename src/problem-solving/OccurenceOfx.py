l = [1,2,6,3,1,7,1,4]
x = 1
print(l.count(x))

c = 0
for i in range(0,len(l)) :
    if x == l[i] :
        c = c+1

print(c)