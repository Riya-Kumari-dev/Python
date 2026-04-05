l = [98,6,53,87,2,60]
l2 = ["Aditi","Notebook",87.4,12]
# l = l+34 # error
l = l+l2 # extend by l2
print(l)

# repetition operator
print(l*3) # repeat l 3 times
print(l) # original as it is 

# comparison
l = [98,6,53,87,2,60]
l3 = [98,6,53,87,2,60]
print(l == l3) # checks all the elements are same in order and of same length

l3[3] = 45
l3[5] = 65
print(l<l3) # compare with the 1st coming difference
print(l>=l3)