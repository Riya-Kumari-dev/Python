l = [1,3,8,10]
sum = 0
for x in l :
    sum += x

print("Sum of all the elements in",l,"is",sum)

l2 = eval(input("Enter a list : ")) # eval function itself evaluates the type of data structure as per the input
# [4,352,"tiya"] / [42,53,12] => seeing a [] => list
# {2,4,1} / {4,2,"tiaya"}=> {} => set
# (3,2,"ity") / (43,23,12)=> () => tuple
# {1:65,2:98,3:87} /{1:"tia",3:65,5:2+4j}=> dict
print(type(l2))
sum = 0
for x in l2 :
    sum += x

print("Sum of all the elements in",l2,"is",sum)
