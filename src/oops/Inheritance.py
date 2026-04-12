class Parent :
    def __init__(self,x,y,z) :
        self.x = x
        self.y = y
        self.__z = z # private cannot inherit by child class
    def display(self) :
        print("x =",self.x)
        print("y =",self.y)

class Child(Parent) :
    def __init__(self,x,y,z,a,b) :
        super().__init__(x,y,z)
        self.a = a
        self.b = b
    def print(self) :
        print("x =",self.x)
        print("y =",self.y)
        # print("z =",self.z) # error cannot access
        print("a =",self.a)
        print("b =",self.b)
    
c = Child(10,20,30,40,50)
c.display() # parent class method
c.print()