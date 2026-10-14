balance = 1000
while True:
    print("=============AKIBA BANK=============")
    print('''    1. Check Balance
    2. Deposit Money
    3. Withdraw Money
    4. Exit
    ''')
    option = int(input("Choose an option: "))
    if option == 1:
        print(f"Your current Balance is:  {balance} Birr")
    elif option == 2:
        deposit = int(input("Enter deposit amount: "))
        print("Deposit successful!")
        balance += deposit
        print(f"Your current balance is: {balance} Birr")
    elif option == 3:
        withdraw = int(input("Enter withdrawal amount: "))
        if withdraw < balance:
            print("Withdrawal Successful!")
            balance -= withdraw
            print(f"Your new balance is: {balance} Birr")
        else:
            print("Insufficient balance!")
    elif option == 4:
        print('''Thank you for using Akiba Bank.
        Goodbye!''')
        break
    else:
        print('''invalid Option.
        Please choose a valid option.''')
        
