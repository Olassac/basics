class BankAccount:
    def __init__(self,accountNumber,name,balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance
# Create the Deposit Method
    def Deposit(self):
        print("Enter deposit amount")
        amount = int(input())
        print("Thank you", amount, "has been successfully deposited in your account \n Kindly take your card")
# Create the Withdrawal Method
    def Withdrawal(self):
        print("""
        Enter 1>>> 1000
        Enter 2>>> 5000
        Enter 3>>> 10000
        Enter 4>>> 20000
        Enter 5>>> other amount
        """)
        #Collect user choice
        user = int(input())
        if user == 1:
            print("Kindly take your cash")
            print("Would you like to buy airtime \n Enter 1>>> Yes \n Enter 2>>> No")
            airtime = int(input())
            if airtime == 1:
                print("Kindly type in the amount")
                amount = int(input())
                print("Enter mobile number")
                mobile = int(input())
                print("The amount of",amount,"has been successfully recharged to",mobile)
                print("Kindly remove your card")
            elif airtime ==2:
                print("Kindly remove your card")
            else:
                print("Wrong input \n Kindly remove your card")
        elif user == 2:
            print("Kindly take your cash")
            print("Would you like to buy airtime \n Enter 1>>> Yes \n Enter 2>>> No")
            airtime = int(input())
            if airtime == 1:
                print("Kindly type in the amount")
                amount = int(input())
                print("Enter mobile number")
                mobile = int(input())
                print("The amount of", amount, "has been successfully recharged to", mobile)
                print("Kindly remove your card")
            elif airtime == 2:
                print("Kindly remove your card")
            else:
                print("Wrong input \n Kindly remove your card")
        elif user == 3:
            print("Kindly take your cash")
            print("Would you like to buy airtime \n Enter 1>>> Yes \n Enter 2>>> No")
            airtime = int(input())
            if airtime == 1:
                print("Kindly type in the amount")
                amount = int(input())
                print("Enter mobile number")
                mobile = int(input())
                print("The amount of", amount, "has been successfully recharged to", mobile)
                print("Kindly remove your card")
            elif airtime == 2:
                print("Kindly remove your card")
            else:
                print("Wrong input \n Kindly remove your card")
        elif user == 4:
            print("Kindly take your cash")
            print("Would you like to buy airtime \n Enter 1>>> Yes \n Enter 2>>> No")
            airtime = int(input())
            if airtime == 1:
                print("Kindly type in the amount")
                amount = int(input())
                print("Enter mobile number")
                mobile = int(input())
                print("The amount of", amount, "has been successfully recharged to", mobile)
                print("Kindly remove your card")
            elif airtime == 2:
                print("Kindly remove your card")
            else:
                print("Wrong input \n Kindly remove your card")
        elif user == 5:
            amount = int(input("Enter amount"))
            print("Kindly take your cash")
            print("Would you like to buy airtime \n Enter 1>>> Yes \n Enter 2>>> No")
            airtime = int(input())
            if airtime == 1:
                print("Kindly type in the amount")
                amount = int(input())
                print("Enter mobile number")
                mobile = int(input())
                print("The amount of", amount, "has been successfully recharged to", mobile)
                print("Kindly remove your card")
            elif airtime == 2:
                print("Kindly remove your card")
            else:
                print("Wrong input \n Kindly remove your card")
        else:
            print("Wrong input \n Kindly remove your card")
    # Create BankFees method
    def BankFees(self):
        result = 5*self.balance/100
        print("Your bank fee charges is", result)
    # Create Display Method
    def Display(self):
        print(self.accountNumber,self.name,self.balance)
# Creating an object
Account = BankAccount(1234567890,"Emmanuel Adedapo Babajide",121350)
Account.Deposit()
