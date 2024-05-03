from bank_x import Bank
from users import Account_holder, Admin

dbbl = Bank("Dutch","Khulna")

while True:
    print("1.Create a bank account")
    print("2. Create an account as an Admin")
    print("3. Log in as ADMIN")
    print("4. Log in as user")
    print("5.. Exit")
    option = int(input("Enter your key(1/2/3/4/5) : "))
    if option == 1:
        print("For creating your bank account provide following information")
        name = input("Enter your username : ")
        password = input("Enter your password: ")
        phone = input("Enter your phone number: ")
        email = input("Enter your email: ")
        address = input("Enter your address: ")
        account_type = input("Enter your account type (savings/current): ")

        user = Account_holder(name=name,password=password,phone=phone,email=email,address=address,account_type=account_type)
        dbbl.generate_account(user)
        print("Welcome as a dbbl user")
        print("please log in for other options")
    
    elif option == 2:
    
        print("For creating your ADMIN account provide following information")
        name = input("Enter your username : ")
        password = input("Enter your password: ")
        phone = input("Enter your phone number: ")
        email = input("Enter your email: ")
        address = input("Enter your address: ")
        

        admin = Admin(name=name,password=password,phone=phone,email=email,address=address)
        dbbl.generate_account(admin)
        print("Welcome as an DBBL Admin")
        print("please log in for other options")
        
        

    elif option == 3:
        username = input("Enter your username : ")
        password = input("Enter your password : ")
        for username in dbbl.account_holders.keys():
            if username == dbbl.account_holders[username].name and password == dbbl.account_holders[username].password:
                while True:
                    print(f"****WELCOME Admin Mr. {dbbl.account_holders.name}****")
                    print("Choose your option as an Admin !")
                    print("1. Delete any user account")
                    print("2. See all user accounts list")
                    print("3. Check the total available balance of the bank")
                    print("4. Check the total loan amount")
                    print("5. On or off the loan feature of the bank")
                    print("6. Log out")
                    choice = int(input("Enter your choice : "))
                    if choice == 1:
                        account_holder_name = input("Enter Account holder name : ")
                        admin.delete_any_account(dbbl, lower(account_holder_name))
                    elif option == 2:
                        admin.all_users(dbbl)
                    elif option == 3:
                        admin.total_balance_of_bank(dbbl)
                    elif option == 4:
                        admin.total_loan_of_bank(dbbl)
                    elif option == 5:
                        print("To turn off/on Loan feature")
                        p = int(input("Enter 1 for on and 2 for off"))
                        if p == 1:
                            admin.control_loan(dbbl,'yes')
                        elif p == 2:
                            admin.control_loan(dbbl,'no')

                    elif option == 6:
                        break;
                    else:
                        print("Invalid input")
            else:
                print("Account does not exist")


    elif option == 4:
        username = input("Enter your username : ")
        password = input("Enter your password : ")
       
        for username in dbbl.account_holders.keys():
            if username == dbbl.account_holders[username].name and password == dbbl.account_holders[username].password:
                while True:
                    print("Choose you option as a user")
                    print("1. Deposit money")
                    print("2. Withdraw money")
                    print("3. Check balance")
                    print("4. Check Transaction History")
                    print("5. Take Loan")
                    print("6. Transder Money")
                    print("7. Log out")

                    x = int(input("Enter your choice please : "))

                    if x == 1:
                        amount = int(input("Enter amount : "))
                        user.deposit_money(dbbl,amount)
                    elif x == 2:
                        amount = int(input("Enter amount : "))
                        user.withdraw_money(dbbl, amount)
                    elif x == 3:
                        user.check_balance(dbbl)
                    elif x == 4:
                        print(user.transaction_history[user.name])
                    elif x == 5:
                        amount = int(input("Enter loan amount : "))
                        user.give_me_loan(dbbl,amount)
                    elif x == 6:
                        reciver = input("enter receiver account name : ")
                        amount = int(input("Enter amount : "))
                        user.send_money(dbbl, receiver, amount)
                    elif x == 7:
                        break
                    else:
                        print("invalid Input")
            else:
                print("Account does not exist")
    elif option == 5:
        break
    else:
        print("Invalid input")  