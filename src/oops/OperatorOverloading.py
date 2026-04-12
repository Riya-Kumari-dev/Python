import math
class Fraction :
    def __init__(self,num,den=1) :
        self.num = num
        self.den = den if den != 0 else print("Please enter a valid denominator")

    # every class inherits Object class 
    # here we are overloading the + operator i.e. polymorphism => one instance/function different actions
    def __add__(self,f) : # __add__ is an object method i.e. it is a usual + operator work does
        new_num = self.num*f.den + self.den*f.num
        new_den = self.den*f.den
        a = Fraction(new_num, new_den)
        return a
    def __sub__(self,f) : # for '-'
        new_num = self.num*f.den - self.den*f.num
        new_den = self.den*f.den
        b = Fraction(new_num, new_den)
        return b
    def __str__(self) : # it is the usual print() method
        # normalize
        gcd = math.gcd(self.num,self.den)
        self.num //= gcd
        self.den //=gcd
        # if both are negative then overall positive
        if self.num < 0 and self.den < 0 :
            self.num = -self.num
            self.den = -self.den
        return str(self.num)+'/'+str(self.den)

f1 = Fraction(2,3)
f2 = Fraction(3,4)
f3 = f1+f2
print(f3)
f4 = f1-f2
print(f2)