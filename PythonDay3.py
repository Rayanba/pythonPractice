balance = 5000
def ATM():
    currentBalance = balance

    print("""Welcome to My Bank
    Please enter one of the following choices:
    [C]eck balance
    [W]ithdraw
    [D]eposit
    [T]ransfer
    [E]xit """)


    while True:
        choice = input("> ")
        if choice.upper() == "C":
            check(currentBalance)
        elif choice.upper() == "W":
            while True:
                cash = int(input("Enter amount to withdraw> "))
                if cash > 0:
                    currentBalance = withdraw(cash, currentBalance)
                    break
                else:
                    print("Enter an integer value")

        elif choice.upper() == "D":
            cash = int(input("Enter amount you want to deposit>"))
            if cash > 0:
                currentBalance = (deposit(cash, currentBalance))
            else:
                print("Enter an integer value")

        elif choice.upper() == "T":
            cash = int(input("Enter amount of money to transfer>"))
            currentBalance = transfer(cash, currentBalance)

        elif choice.upper() == "E":
            print("Exiting....")
            print("Thank you for using My Bank ATM")
            break
        else:
            print('Incorrect input')

def withdraw(cash, currentBalance):
    if(cash<=currentBalance):
        currentBalance = currentBalance - cash
        print(f"Dispensing the amount {cash}")
        print(f"Remaining balance is: {currentBalance}")
    else:
        print("No sufficient funds!")
        print("Try another option or [E]xit")
    return currentBalance

def deposit(cash, currentBalance):
    currentBalance += cash;
    print(f"your new balance is: {currentBalance}")
    return currentBalance

def transfer(cash, currentBalance):
    if cash > currentBalance:
        print ("you don't have that amount in you wallet")
    elif cash > 0:
        currentBalance -= cash
        print(f"The transfer has been done successfully\n Remaining balance is: {currentBalance}")

    else:
        print("Enter an integer value")
    return currentBalance

def check(currentBalance):
    print(f"Your current balance is: {currentBalance}")
    return 0

ATM()