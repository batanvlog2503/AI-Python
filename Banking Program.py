
# Python Banking Program
balance = 0
def show_balance():
    print(f'Your balance is ${balance:.2f}')
def deposit():
    amount = float(input("Enter an amount to be deposited: "))
    if amount < 0:
        print("That's not a valid answer")
        return 0
    else:
        return amount
def withdraw():
    amount = float(input("Enter an amount to be withdraw: "))

    if amount > balance:
        print("Overcome accoune balance")
        return 0
    else:
        return amount


request = True

while request:
    print("-------Banking Program-------")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice (1 - 4): ")
    if choice == '1':
        show_balance()
    elif choice == '2':
        balance += deposit()
    elif choice == '3':
        balance -= withdraw()
    elif choice == '4':
        request = False
    else:
        print("That is not a valid choice")