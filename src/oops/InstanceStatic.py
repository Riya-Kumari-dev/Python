class Student :
    institute = "Amity University" # static variable
    # static variable => 1 copy
    def __init__(self,naam,c,id) :
        # here name,course, id is instance variable 
        # while naam,c, id is local variable
        self.name = naam
        self.course = c
        self.id = id
    def display(self) : 
        # this is instance method 
        # Instance Method : A function defined inside a class that operates on a specific instance(object) of that class
        print("Name :",self.name)
        print("Course :",self.course)
        print("Id :",self.id)

    # class method
    # inside any method only class variable/static variable are used => class method
    # for every class, class level object is created in which all the static variables and class method information is stored
    @classmethod
    def displayclass(cls) : # cls is referring to that class object
        print(cls.institute)

    # static method
    # Method that belongs to class but does not have access to any instance-specific (self) or class specific (cls) data
    @staticmethod
    def fun(a,b,c) :
        print(a,b,c)

s = Student("Riya Kumari","BCA",4)
s.display()
s2 = Student("Aditi Kumari","Btech",5)
s2.display()
print(Student.institute) # can be access with the class name
Student.displayclass()
# static methods can be access through class name or instance 
s.fun(2,3,1)
Student.fun(10,2,3)