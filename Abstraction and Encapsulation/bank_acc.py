#"- Create a `BankAccount` class with private attributes for `account_number` and `balance`.
# - Add methods to check balance, deposit, and withdraw funds.
# - Try accessing the balance directly and observe the result.
class Bank:
    def __init__(self,balance):
        self.__balance=balance
        
    def deposit(self,amount):
        if amount>=0:
            self.__balance+=amount
            print(f"{amount} Credited to ur acc Your current Bank Balance is {self.__balance}")
        else:
            print("Please the valid amount and negative value is not allowed")
        
    def withdraw(self,amount):
        if amount>=0:
            self.__balance-=amount
            print(f"{amount} debited from ur bnk account Your Current Bank Balance is {self.__balance}")
        else:
            print("Please the valid amount and negative value is not allowed")
acc=Bank(1000)
acc.balance=1234
acc.deposit(1000)
acc.withdraw(200)
