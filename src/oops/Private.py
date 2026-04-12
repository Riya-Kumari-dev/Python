class Employee :
    def __init__(self,name,age) :
        self.name = name
        self.age = age
        self.__salary = 320000 # private
    def marriage(self,wife) : # only add on calling the function
        self.wife = wife
    
e = Employee("Aditya",23)
# print(e.salary) # ❌ cannot access
# print(e.wife) # till now no attribute 'wife'
e.marriage("Aditi") # now 'wife' added
print(e.wife)