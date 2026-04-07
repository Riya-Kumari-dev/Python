d = {1:"Riya",2:"Aditi",3:[3,7,2],4:{3:"Nitya",4:"Jhalak"},5:"Riya"}
print(d)
print(d[1])  # Riya
print(d[3]) # [3, 7, 2]
# print(d[100]) # error if not present

print(d.get(1)) # Riya
print(d.get(4)) # {3: 'Nitya', 4: 'Jhalak'}
print(d.get(1010)) # None
print(d.get(100,0)) # if 100 is present as key then it will return its value else return 0 # 0

for x in d :
    print(x,d[x])
# 1 Riya
# 2 Aditi
# 3 [3, 7, 2]
# 4 {3: 'Nitya', 4: 'Jhalak'}
# 5 Riya


print(d.keys()) # dict_keys([1, 2, 3, 4,5])
print(d.values()) # dict_values(['Riya', 'Aditi', [3, 7, 2], {3: 'Nitya', 4: 'Jhalak'},'Riya'])
print(d.items()) # dict_items([(1, 'Riya'), (2, 'Aditi'), (3, [3, 7, 2]), (4, {3: 'Nitya', 4: 'Jhalak'}), (5, 'Riya')])