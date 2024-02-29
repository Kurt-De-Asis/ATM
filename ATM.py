print("Welcome to Banku.Ph")
print("What would you like to do?")
while True:
    balance = 525426
    savings = 200_000
    choose = (input("1. Check Balance.\n2. Check Savings.\n3. Withdraw.\n4. Deposit.\n5. Exit.\ninput:"))
    if choose == '1':
        print("Your remaining balance is: $" + str(balance))
        choice1 = input("Would you like to do another transaction? (Y/N): ")
        if choice1.upper() == 'Y':
            print("Welcome to Banku.Ph")
            print("What would you like to do?")
        else:
            print("Thank you for using Banku.Ph!")
            exit()
    elif choose == '2':
        print("Your savings amount is: $" + str(savings))
        choice1 = input("Would you like to do another transaction? (Y/N): ")
        if choice1.upper() == 'Y':
            print("Welcome to Banku.Ph")
            print("What would you like to do?")
        else:
            print("Thank you for using Banku.Ph!")
            exit()
    elif choose == '3':
        withdraw = int(input("How much would you like to withdraw?: $"))
        if withdraw > balance:
            print("Not enough balance")
        else:
            remain = balance - withdraw
            choice = input("Your remaining balance after this withdrawal will be $" + str(remain) + " Confirm? (Y/N): ")
            if choice.upper() == 'Y':
                print("You succesfully withdraw $"+str(withdraw))
            choice1 = input("Would you like to do another transaction? (Y/N): ")
            if choice1.upper() == 'Y':
                print("Welcome to Banku.Ph")
                print("What would you like to do?")
            else:
                print("Thank you for using Banku.Ph!")
                exit()
    elif choose == '4':
        deposit = int(input("How much would you like to deposit?: $"))
        add_balance = deposit + balance
        print("Success! Your remaining balance is $" + str(add_balance))
    elif choose == '5':
        print("Thank you for using Banku.Ph!")
        exit()
    elif choose.isalpha():
        print("Invalid. Please enter the right number")
    else:
        print("Invalid choice.")
