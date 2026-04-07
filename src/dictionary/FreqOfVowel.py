s = "Riya Gupta"
l = list(s)
d = {}
for ele in l : 
    if ele in 'aeiouAEIOU' :
        d[ele] = d.get(ele,0)+1

print(d) # {'i': 1, 'a': 2, 'u': 1}