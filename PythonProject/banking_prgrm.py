def show_balance():
    print("-----------------------------")
    print(f"you are having -->{balance}$")
    print("-----------------------------")

def deposit():
    amount =(int(input('enter amount to deposit :')))
    if  amount < 0:
        print("negative amount can't be added ")
        return 0
    elif amount > 100000:
        print("you must need a pan card to add more than a lakh")
        return 0
    else:
        print("------------------------------------")
        print(f"Deposit of {amount} is successfull!")
        print("------------------------------------")
        return amount

def withdraw():
    amount = int(input("enter amount :"))
    if amount < 0:
        print("amount should be greater than '0' ")
        return 0
    elif amount > balance:
        print("insufficient balance !!")
        return 0
    else:
        print("---------------------------------------------")
        print(f'withdraw of amount {amount}$ is successfull!')
        print("---------------------------------------------")
        return amount

balance = 0
is_running = True

while is_running == True:
    print("|-------------------|")
    print("|  Bank of Baroda   |")
    print("|-------------------|")
    print("|choose any option :|")
    print("|         |         |")
    print("|         v         |")
    print("|1. show balance    |")
    print("|2.deposit          |")
    print("|3.withdraw         |")
    print("|4.exit             |")
    print("|-------------------|")

    choice = int(input("enter your choice: "))

    if choice == 1:
        show_balance()
    elif choice == 2:
        balance += deposit()
    elif choice == 3:
        balance -= withdraw()
    elif choice == 4:
        is_running == False
        print("Thank you Have a nice day!!")
        break
    else:
        print("please enter a valid choice!!")





