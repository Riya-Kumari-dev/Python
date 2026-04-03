# except for the last word iterate through each word and take only its first letter
name = "Amar Nath Singh"
a = name.split()
l = []
for word in a[:len(a) -1] : # iterate till the second last
    l.append(word[0])

updated = ".".join(l)
updated += " "+a[len(a)-1]
print(updated)