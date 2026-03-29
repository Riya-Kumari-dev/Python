marks = int(input("Enter your percentage of marks : "))
if(marks >= 90):
    print("A+")
    print("Excellent")
elif(marks < 90 and marks >= 80):
    print("A")
    print("Very Good")
elif(marks < 80 and marks >=70):
    print("B+")
    print("Good")
elif(marks < 70 and marks >= 60):
    print("B")
    print("Need improvement")
elif(marks < 60 and marks >=50):
    print("C")
elif(marks < 50 and marks >= 40):
    print("D")
else :
    print("Fail")
    print("Reattempt")