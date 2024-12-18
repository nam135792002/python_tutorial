# Python Banking Program

def show_balance(balance):
    print(f"Your balance is {balance:,.0f} VND")

def deposit() -> int:
    amount = int(input("Enter an amount to be deposited: "))
    
    if amount < 0:
        print("That's not a valid amount")
        return 0
    else:
        return amount

def withdraw(balance) -> int:
    amount = int(input("Enter amount to be withdrawn: "))
    
    if amount > balance:
        print("Insufficint funds")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount

def main():
    current_balance = 1000000
    is_running = True

    while is_running:
        print("Banking Program")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withraw")
        print("4. Exit")
        
        choice = input("Enter your choice(1-4): ")

        if choice == '1':
            show_balance(current_balance)
        elif choice == '2':
            current_balance += deposit()
        elif choice == '3':
            current_balance -= withdraw(current_balance)
        elif choice == '4':
            is_running = False
        else:
            print("That is not a valid choice")

if __name__ == '__main__':
    main()
