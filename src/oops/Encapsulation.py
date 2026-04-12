class Account :
    def __init__(self,balance=2000) :
        self.__balance = balance # private cannot access outside the class
        # can be access using setter and getters
    
    # setter
    def withdraw(self,amount) :
        if self.__balance >= amount :
            self.__balance -= amount
        else :
            print("Insufficient balance for the request to complete")
    def deposit(self,amount) :
        self.__balance += amount
    # getter
    def checkBalance(self) :
        print("Total Balance : ",self.__balance)
    
a = Account()
a.deposit(3000)
a.checkBalance()
a.withdraw(100)
a.checkBalance()