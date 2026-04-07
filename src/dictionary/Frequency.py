s = "This is a very legitimate story about a renowned person. He is very humble and renowned for his honesty."
wordsList = s.split()
d = {}
# for word in wordsList :
#     if word in d : 
#         d[word] = d[word] + 1
#     else :
#         d[word] = 1

for word in wordsList :
    d[word] = d.get(word,0) + 1

print(d)