class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.__balance=balance
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            return(f"Deposited {amount}. New balance: {self.__balance}")
        return "Invalid deposit"
    def withdraw(self, amount):
        if 0<amount<=self.__balance:
            self.__balance-=amount
            return(f"Withdrew {amount}. New balance: {self.__balance}")
        return("Invalid withdrawal")
    def get_balance(self):
        return self.__balance
acc1=BankAccount("Munna",200000)
acc1.deposit(1000)
print("After deposit: ",acc1.get_balance())
acc1.withdraw(1000)
print("After withdraw: ",acc1.get_balance())