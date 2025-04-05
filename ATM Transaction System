# 12. ATM Transaction System

class Bank:
    def __init__(self, balance):
        self.balance = balance

    def depositMoney(self, money):
        self.balance = self.balance + money

    def withdrawMoney(self, money):
      if money > self.balance:
        print("insufficient balance")
      else:
        self.balance = self.balance - money

    def displayBalance(self):
        return self.balance

b1 = Bank(20000)
print("1. check balance\n2. Deposit money\n3. withdraw money\n4. exit the system\n")
ch = int(input("enter the choice: "))

if ch == 1:
    s = b1.displayBalance()
    print("available balance: ",s)
elif ch == 2:
    m = int(input("enter money: "))
    b1.depositMoney(m)
    print("money is deposited successfully")
    s = b1.displayBalance()
    print("now availble balance is: ",s)
elif ch == 3:
    m = int(input("enter money: "))
    b1.withdrawMoney(m)
    print("money is withdraw successfully")
    s = b1.displayBalance()
    print("now availble balance is: ",s)
elif ch == 4:
    print("exit")
else:
    print("enter valid choice")
