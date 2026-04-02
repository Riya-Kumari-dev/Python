# print only odd

for i in range(1,101) : 
    if i%2 == 0 :
        continue # skip the remaining portion of the current iteration
    print(i,end = " ")