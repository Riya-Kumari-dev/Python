# seperator => by default python add " " (space) as seperator
a = 10
b = 20
c = 30
print(a,b,c) # 10 20 30
print(a,b,c,sep='#') # 10#20#30
print(a,b,c,sep = '@') # 10@20@30

# end attribute => by default end = '\n' (new line)
print("Hello")
print("Everyone") 
# Hello
# Everyone

print("Hello",end = ' ')
print("Everyone",end = ' ')
print("Kaise ho")
# Hello Everyone Kaise ho