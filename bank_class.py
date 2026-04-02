class bank_account :
    def __init__(self):
        self.name = input ("Enter Account Hoder's Name: ")
        self.__balance = float (input ("Enter Initial Balance: $"))
    def deposit(self):
        amount = float (input ("Enter Amount to Deposit : "))
        if amount > 0 :
            self.__balance += amount
            print (f"Deposited ${amount :2f} Your current balance is ${self.__balance :2f}")
        else :
            print ("Deposit must be above 0$")
    def withdraw(self):
        amount = float (input ("Enter amount to withdraw : "))
        if amount > 0 and amount <= self.__balance :
            self.__balance -= amount
            print (f"Withdraw success amount ${amount :2f} Your current balance is ${self.__balance :2f}")
        elif amount > self.__balance :
            print ("Not enough balance!")
        else :
            print ("Withdeaw must be above 0$")
    def check(self):
        print (f"Account Holder's name : {self.name}")
        print (f"Current Balance : ${self.__balance : 2f}")
if __name__ == "__main__":account = bank_account()
while True :
    print ("1. Deposit")
    print ("2. WIthdraw")
    print ("3. Check Balance")
    print ("4. Exit")
    ch = int (input ("Entrt your choice : "))
    if ch == 1:
        account.deposit()
    elif ch == 2:
        account.withdraw()
    elif ch == 3:
        account.check()
    elif ch == 4:
        break
    else:
        print ("Invalid choice!")