from abc import ABC, abstractmethod

class RBI(ABC) :
    # if a class has even one abstract method then the class is abstract class
    # we cannot create instance of an abstract class
    # the child class must define the abstract method of the parent class
    def __init__(self) :
        print("RBI")
    @abstractmethod
    def minBalance(self) :
        pass
    def f(self) :
        print("Hahaa")

class ICICI(RBI) :
    def __init__(self) :
        print("ICICI")
    def minBalance(self) :
        print("Implented minBalance")
    def fun(self) :
        print("Child class method")
    
c = ICICI()
c.f()
c.minBalance()
c.fun()