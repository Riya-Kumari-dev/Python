try :
    l = [3,2,6,3]
    i = int(input("Enter the index : "))
    if i >= len(l) :
        raise IndexError
    b = l[i]
    print(b)
except IndexError :
    print("Please enter a valid index")