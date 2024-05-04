from bank_x import Bank
from users import Account_holder, Admin

dbbl = Bank("Dutch","Khulna")

# user1 = Account_holder('tahmid','1234','12323332','tahmid@gmail.com','khulna','savings')
# user2 = Account_holder('tanzim','etr4','12323332','tanzim@gmail.com','khulna','savings')
# user3 = Account_holder('samim','eree34','12323332','samim@gmail.com','khulna','savings')

admin = Admin('admin','123','12323332','samim@gmail.com','khulna')

dbbl.generate_account(admin)

# user1.deposit_money(dbbl,3000)
# user1.withdraw_money(dbbl,300)
# user1.check_balance(dbbl)
# user1.send_money(dbbl,'tanzim',400)
# user1.give_me_loan(dbbl,400)
# # user1.check_transaction_history()
# # user2.check_transaction_history()
# admin.all_users(dbbl)
# admin.delete_any_account(dbbl,'tanzim')
# admin.all_users(dbbl)
# admin.total_balance_of_bank(dbbl)
# admin.total_loan_of_bank(dbbl)
# admin.control_loan(dbbl,'yes')
# admin.control_loan(dbbl,'no')




while True:
    print("1.Create a bank account")
    print("2. Log in as ADMIN")
    print("3. Log in as user")
    print("4.. Exit")
    option = int(input("Enter your key(1/2/3/4) : "))
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
        username = input("Enter your username : ")
        password = input("Enter your password : ")
        
        if username == dbbl.account_holders[username].name and password == dbbl.account_holders[username].password:
            while True:
                print(f"\t\n****WELCOME Admin Mr. {dbbl.account_holders[username].name}****")
                print("Choose your option as an Admin !")
                print("1. Delete any user account")
                print("2. See all user accounts list")
                print("3. Check the total available balance of the bank")
                print("4. Check the total loan amount")
                print("5. On or off the loan feature of the bank")
                print("6. Log out")
                choice = int(input("\t\nEnter your choice : "))
                if choice == 1:
                    account_holder_name = input("\t\nEnter Account holder name : ")
                    admin.delete_any_account(dbbl, account_holder_name)
                elif choice == 2:
                    admin.all_users(dbbl)
                elif choice == 3:
                    admin.total_balance_of_bank(dbbl)
                elif choice == 4:
                    admin.total_loan_of_bank(dbbl)
                elif choice == 5:
                    print("To turn off/on Loan feature")
                    p = int(input("\t\nEnter 1 for ON and 2 for OFF: "))
                    if p == 1:
                        admin.control_loan(dbbl,'yes')
                    elif p == 2:
                        admin.control_loan(dbbl,'no')

                elif choice == 6:
                    break;
                else:
                    print("Invalid input")
        else:
            print("\t\n Account does not exist")


    elif option == 3:
        username = input("\t\nEnter your username : ")
        password = input("\t\nEnter your password : ")
       
        if username == dbbl.account_holders[username].name and password == dbbl.account_holders[username].password:
            while True:
                print("\t\n Choose you option as a user")
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
                    user.check_transaction_history()
                elif x == 5:
                    amount = int(input("Enter loan amount : "))
                    user.give_me_loan(dbbl,amount)
                elif x == 6:
                    receiver = input("enter receiver account name (in lower case): ")
                    amount = int(input("Enter amount : "))
                    user.send_money(dbbl, receiver, amount)
                elif x == 7:
                    break
                else:
                    print("invalid Input")
        else:
            print("Account does not exist")
    elif option == 4:
        break
    else:
        print("Invalid input")  