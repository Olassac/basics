byebye = "Thank you for banking with us \n Kindly take your card"
print("Good morning, Welcome to Olamide Bank")
print("""
Enter 1>> New User
Enter 2>> Old User
""")
user = int(input())
if user == 1:
    print("Press 1 to create new account")
    create = int(input())
    if create ==1:
        print("Collect details")
        details = input()
        print("""
        Congratulations you have successfully created an account
        Your new account number is 123456789
        """)
        print("Do you want to deposit?")
        print("""
        Enter 1>>> Yes
        Enter 2>>> No
        """)
        deposit = int(input())
        if deposit == 1:
            print("deposit amount")
            amount = (int(input()))
            print("You have successfully deposited", amount)
            print("'press 1 to continue")
            cont = (int(input()))
            if cont == 1:
                print("would you like to buy airtime")
                print("""
                Enter 1>>> Yes
                Enter 2>>> No
                """)
                airtime = int(input())
                if airtime == 1:
                    print("airtime successful")
                    print(byebye)
                elif airtime == 2:
                    print(byebye)
            else:
                print(byebye)

        else:
            print(byebye)
    else:
        print(byebye)

elif user == 2:
    print("Service temporarily unavailable")
    print("Would you like to buy airtime")
    print("""
    Enter 1>>> Yes
    Enter 2>>> No
    """)
    airtime = int(input())
    if airtime == 1:
        print("Here is your recharge card")
    else:
        print(byebye)