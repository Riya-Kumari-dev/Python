class Teacher :
    '''This is a doc string'''
    def __init__(self) :
        self.name = "Riya Gupta" # initializes the object variables
        self.age = 22
    def display(self) :
        print("Name :",self.name)
        print("Age :",self.age)
    

t = Teacher()
# to access the properties or methods of class tempelate we must have a real entity i.e. object
# Teacher()
# 1) creates the object of Teacher class
# 2) __init__ executes (constructor)
# t = Teacher()
# t is the reference to object created

print(t.__doc__) # access the object's doc string
t.display()