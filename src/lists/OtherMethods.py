l = ["Riya","Aditi",45.3,98,32,"tanya"]

# index(ele)
# returns the 1st occurence of ele if not present gives error
print(l.index("Aditi")) # 1
# print(l.index("aditi")) # error
# to be safe first check if present by membership operator
if "Aditi" in l : 
    print("Aditi is present at index",l.index("Aditi"),"in",l)
else : 
    print("Aditi is not present in",l)

# reverse
l.reverse() # ['tanya', 32, 98, 45.3, 'Aditi', 'Riya']
print(l) 

# sort
# l.sort() # error => ele should be of same type

l2 = [45,98,10,-43,76.4]
l2.sort() # increasing order [-43, 10, 45, 76.4, 98]
print(l2)
l3 = ["aam","Bam","camera","Disco"]
l3.sort() # ['Bam', 'Disco', 'aam', 'camera']
print(l3)

# sort in decreasing order
l3.sort(reverse=True) # ['camera', 'aam', 'Disco', 'Bam']
print(l3)