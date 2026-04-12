import math
class Fraction :
    def __init__(self,num,den=1) :
        self.num = num
        self.den = den if den != 0 else print("Please enter a valid denominator")
    def add(self,f) :
        self.num = self.num*f.den + self.den*f.num
        self.den = self.den*f.den
        self.display()
    def sub(self,f) :
        self.num = self.num*f.den - self.den*f.num
        self.den = self.den*f.den
        self.display()
    def mul(self,f) :
        self.num *= f.num
        self.den *= f.den
        self.display()
    def div(self,f) :
        self.num *= f.den
        self.den *= f.num
        self.display()
    def display(self) :
        # normalize
        gcd = math.gcd(self.num,self.den)
        self.num //= gcd
        self.den //=gcd
        # if both are negative then overall positive
        if self.num < 0 and self.den < 0 :
            self.num = -self.num
            self.den = -self.den
        print(self.num,'/',self.den,sep='')

f1 = Fraction(2,3)
f2 = Fraction(3,4) 
f1.add(f2) # f1 = 17/12
f2.sub(f1) # f2 = -8/12 => -2/3
f1.mul(f2) # f1 = -17/18
f2.div(f1) # 12/17

f3 = Fraction(2,0) # Please enter a valid denominator
f4 = Fraction(2)
f4.display() # 2/1