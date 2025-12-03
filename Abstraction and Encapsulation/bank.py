class Bank:
    def __init__(self,balance):
        self.__balance=balance
    def balance(self):
        print(self.__balance) #By Using Getters we Retrieving the balance
    def update(self,balance):
        self.__balance=balance #Using setters we updating a balance
    def deposit(self,amt):
        if amt >0:
            self.__balance+=amt
            print(self.__balance)
        else:
            print("Amt should be in Positive") 
    def withdraw(self,amt):
        if amt>0:
            self.__balance-=amt
            print(self.__balance)
        else:
            print("Positive nmbers only")   
        
a=Bank(15000)
a.balance()#Here We called the function in which bank balance is display for users by (Getters)
a.deposit(5000)
a.update(12500)#Here we called the function in which bank balance updated By (Setters)
a.withdraw(12000)

