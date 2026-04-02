for i in range(1,10) :
    if i%5 == 0 :
        break
    print(i)
else : # code will execute only if we came out of the loop without break execution
    print("Hello") # ❌ not execute here

for i in range(1,10) :
    if i%11 == 0 :
        break
    print(i)
else : 
    print("Hello") #execute here

