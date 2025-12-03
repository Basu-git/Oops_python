class Bank:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amt):
        if amt>0:
            self.__balance+=amt
            print(f"The balance {self.__balance}")
        else:
            print("The amt must be in positive")
    def withdraw(self,amt):
        if amt>0:
            self.__balance-=amt
            print(f"Balance is {self.__balance}")
        else:
            print("Amt should be in positive")
a=Bank(15000)
a.deposit(5000)
a.withdraw(12000)

