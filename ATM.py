import openpyxl
from time import sleep
from openpyxl import Workbook, load_workbook

def countDown():
    for i in range(3, 0, -1):
        print(i)
        sleep(1)

def main():
    bank = load_workbook('bankAccounts.xlsx')
    sheet = bank.active

    while True:
        print("Welcome to Online Banking\n"
              "*************************\n"
              "1. Check Balance\n"
              "2. Withdraw\n"
              "3. Deposit\n"
              "4. Exit\n"
              "*************************")
        try:
            choice = int(input("What would you like to do?: "))
        except ValueError:
            print("Invalid input. Please enter a number from the list of choices.")
            continue

        if choice == 1:
            print("Your balance is: $" + str(sheet['E2'].value))
            if input("Would you like to do another transaction? ( y / n) : ").lower() == 'n':
                break
        elif choice == 2:
            withdraw = int(input("How much would you like to withdraw?: $"))
            if withdraw > sheet['E2'].value:
                print("Insufficient funds.")
            else:
                sheet['E2'].value -= withdraw
                print("Thank you for using the ATM! Withdrawing your cash now...")
                countDown()
                print(f"Withdrawal Successful! Your new balance is ${sheet['E2'].value}")
                if input("Would you like to do another transaction? ( y / n) : ").lower() == 'n':
                    break
        elif choice == 3:
            deposit = int(input("How much would you like to deposit?: $"))
            sheet['E2'].value += deposit
            print("Thank you for using the ATM! Depositing your cash now...")
            countDown()
            print(f"Your cash was deposited successfully! Your new balance is ${sheet['E2'].value}")
            if input("Would you like to do another transaction? ( y / n) : ").lower() == 'n':
                break
        elif choice == 4:
            print("Thank you for using my program, have a great day!")
            break
        else:
            print("Please choose in the list of choices!")

    bank.save('bankAccounts.xlsx')

if __name__ == "__main__":
    main()
