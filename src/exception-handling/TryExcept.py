while 1 :
    try :
        a = int(input("Enter the numerator : "))
        b = int(input("Enter the denomenator : "))
        ans = a/b
        print(ans)
        break
    except ValueError :
        print("Please enter a valid number : ")
    except ZeroDivisionError :
        print("Please enter a non-zero value for denominator : ")
    