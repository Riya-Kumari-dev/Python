class Teacher : 
    def __init__(self,name,age) : # Parameterized constructor
        self.name = name # self is like this keyword
        self.age = age
    def display(self) :
        print("Name :",self.name)
        print("Age :",self.age)

t = Teacher() # same as java if we add parameterized constructor and don't add default one it will throw error
t.name = "Aditi Mishra"
t.age = 25
t.display()
t2 = Teacher("Riya Gupta",24)
t2.display()