class TypoError(Exception) :
    pass
try :
    a = int(input("Enter a non-negative number : "))
    if a<0 :
        raise TypoError 
    print(a)
except TypoError :
    print("Please enter a non-negative number.")