s = "Riya Gupta"
t = "Riya"
t = "Tiya"
for i in t :
    if i not in s :
        print("No,",t,"is not a subset of",s)
        break
else :
    print("Yes,",t,"is a subset of",s)