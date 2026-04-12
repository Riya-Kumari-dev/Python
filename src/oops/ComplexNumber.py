class Complex :
    def __init__(self,real=0,imag=0) :
        self.real = real
        self.imag = imag
    def add(self,c) :
        self.real += c.real
        self.imag += c.imag
        self.display()
    def sub(self,c) :
        self.real -= c.real
        self.imag -= c.imag
        self.display()
    def mul(self,c) :
        a = self.real
        b = self.imag
        self.real = a*c.real - b*c.imag
        self.imag = a*c.imag + b*c.real
        self.display()
    def div(self,c) :
        a = self.real
        b = self.imag
        self.real = (a*c.real + b*c.imag) / (c.real*c.real  + c.imag*c.imag)
        self.imag = (b*c.real - a*c.imag) / (c.real*c.real  + c.imag*c.imag)
        self.display()
    def display(self) :
        print(self.real,'+' if self.imag >= 0 else '',self.imag,'i',sep='')

c1 = Complex(2,4)
c2 = Complex(1,5)
c1.add(c2) # c1 = 3+9i
c1.sub(c2) # c1 = 2+4i
c2.mul(c1) # c2 = -18+14i
c2.div(c1) # 1+5i
c3 = Complex(1,-4)
c3.display() # 1-4i