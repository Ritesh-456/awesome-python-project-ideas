def show_balance(balance):
    print("-------------------------")
    print(f"Your Balance is = {balance:,.2f}")

def deposit(balance):
    print("-------------------------")
    amount = float(input("Enter your amount you want to deposit: "))

    if amount <= 0:
        print("-------------------------")
        print("Amount cant zero or less then zero.")
        return 0

    else:
        print("-------------------------")
        print(f"{amount:,.2f} rupees is deposit from your bank account.")
        return amount

def withdrawal(balance):
    print("-------------------------")
    amount = float(input("Enter amount you want to withdrawal: "))
    

    if amount > balance:
        print("-------------------------")
        print(f"Your Balance currently is = {balance:,.2f}")
        print("So, Amount cant zero or less then zero.")
        return 0

    else:
        print("-------------------------")
        print(f"{amount:,.2f} rupees is withdrawal fom your bank account.")
        return amount



def main():
    balance = 0
    is_runnning = True

    while is_runnning:

        print("-------------------------")
        print("!!! Your Bank Details !!!")
        print("-------------------------")

        print("1. Show Balance\n2. Deposit Money\n3. Withdrawal Money\n4. Exit")
        print("-------------------------")
        choice = float(input(f"Enter you choices (1,2,3,4): "))
        options = int(choice)

        if options == 1:
            show_balance(balance)

        elif options == 2:
            balance += deposit(balance)
        
        elif options == 3:
            balance -= withdrawal(balance)

        elif options == 4:
            print("Thank Q for visiting")
            is_runnning == False

        else:
            print("Invalid Input")

    print("Have a nice day")


if __name__ == "__main__":
    main()