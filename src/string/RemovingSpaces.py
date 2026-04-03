s = "   Riya"
print(len(s))
t = s.lstrip() # remove left spaces 
print(len(t))

s = "Riya   "
print(len(s))
t = s.rstrip() # remove right spaces 
print(len(t))

s = "   Riya     "
print(len(s))
t = s.strip() # remove left spaces and right spaces
print(len(t))