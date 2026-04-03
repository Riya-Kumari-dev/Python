# split 
# by default seperator for split s.split(" ") i.e. space 
# returns list of strings

s = "Riya is a nice girl."
l = s.split() 
print(type(l)) # list
print(l) # ['Riya', 'is', 'a', 'nice', 'girl.']

t = "3/04/2026"
l = t.split('/')
print(l) # ['3', '04', '2026']