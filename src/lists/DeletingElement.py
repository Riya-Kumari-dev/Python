l = [54,32,98,76,50,33,32]
print(l)
l.remove(32) # removes the 1st occurence 
print(l)

l.pop() #removes the last element
print(l)

# print(l.remove(74)) # error => not present in the list
print(l.remove(50)) # remove function does not return anything # None
print(l.pop()) # return last element and then remove it # 33
print(l)
print(l.pop(2)) # return the element at index 2 and remove it 