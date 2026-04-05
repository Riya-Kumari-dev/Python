l = []
# list.append(element) => add element to the last  
l.append(10) # 10 
l.append(20) # 20
print(l) 

# list.insert(index,element) 
# => adding element to the index
l.insert(1,30)
print(l)
l.insert(40,23) # 40 no index so it is the largest index possible for right now so it will be added to the last
print(l)

# insert and append only 1 element at a time
# but by extend we are adding element of one list to the end of the other list
a = [3,4,2]
a.extend(l) # we are extending a by l
print(a)
print(l)