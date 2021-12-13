class BankAccount:
    def __init__(self,accountNumber,name,balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance
    def withdrawal(self):
        amount = int(input("Enter amount"))
        if amount <= self.balance:
            print("Kindly take your cash")
        elif amount > self.balance:
            print("Insufficient funds")
Account=BankAccount(12345678,"Bisi",15555)
Account.withdrawal()




