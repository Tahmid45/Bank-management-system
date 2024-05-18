from abc import ABC
from datetime import datetime
class User(ABC):
    def __init__(self, name, password, phone, email, address):
        self.name = name
        self.password = password
        self.phone = phone
        self.email = email
        self.address = address
    

class Account_holder(User):
    def __init__(self, name, password, phone, email, address, account_type):
        super().__init__(name,password, phone, email, address)
        self.account_number = None
        self.account_type = account_type
        self.current_balance = 0
        self.transaction_history_personal = []
    
    def deposit_money(self,bank, amount):
        if bank.bankrupt == True:
            print("Money Deposit is not possible due to bankrupt")
        else:
            self.current_balance += amount
            bank.update_balance(amount)
            print(f"TK {amount} deposited successfully")
    
    def withdraw_money(self,bank, amount):
        if bank.bankrupt == True:
            print("Money withdral is not possible due to bankrupt")
        else:
            if amount > self.current_balance:
                print("Withdrawal amount exceeded!!")
                
            else:
                self.current_balance -= amount
                print(f"withdraw tk {amount}")
                bank.update_balance_for_withdraW(amount)
    def check_balance(self, bank):
        print(bank.account_holders[self.name].current_balance)

    def check_transaction_history(self):
        print(f"Here is your transaction history : {self.transaction_history_personal}")
        

    def give_me_loan(self, bank, amount):
        bank.take_loan(self.name,amount)
        self.current_balance += amount
        bank.update_balance_for_withdraW(amount)
    
    def send_money(self, bank, receiver, amount):
        if amount < self.current_balance:
            bank.transaction(self, receiver, amount)
        else:
            print("Insufficient balance")
                

class Admin(User):
    def __init__(self, name, password, phone, email, address):
        super().__init__(name, password, phone, email, address)

    def delete_any_account(self,bank, name):
        bank.delete_account(name)

    def all_users(self,bank):
        bank.see_all_users()

    def total_balance_of_bank(self, bank):
        bank.total_bank_balance()

    def total_loan_of_bank(self, bank):
        bank.total_bank_loan()

    def control_loan(self, bank, variable):
        if variable == 'yes':
            bank.loan_feature_on()
            print("Loan feature is On")
        elif variable == 'no':
            bank.loan_feature_off()
            print("Loan feature is off")
        else:
            ("Invalid Input")


class Bank:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.account_holders = {}
        self.total_balance = 0
        self.total_loan = 0
        self.bankrupt = False
        self.loan = True
        

    def generate_account(self,account_holder):
        account_id = f"{self.name}-{len(self.account_holders)}"
        account_holder.account_number = account_id
        self.account_holders[account_holder.name] = account_holder
    
    def delete_account(self, name):
        self.account_holders.pop(name)
        print(f"account is deleted {name}")

    def see_all_users(self):
        print("\n\tALL users are Here")
        print(f"name\t phone \t\temail" )
        for key, account in self.account_holders.items():
            if key != 'admin':
                print(f"{account.name}\t {account.phone} \t{account.email}" )
    
    def update_balance(self, amount):
        self.total_balance += amount
    
    
    def update_balance_for_withdraW(self, amount):
        self.total_balance -= amount
    
    def total_bank_balance(self):
        return print(f"Total Balance of the bank : {self.total_balance}")
    
    def total_bank_loan(self):
        return print(f"Total loan amount of the bank : {self.total_loan}")


    def loan_feature_on(self):
        self.loan = True
    
    def loan_feature_off(self):
        self.loan = False
        
    def take_loan(self, name, amount):
        if self.loan == True:
            self.total_loan += amount
            self.total_balance -= amount
            

    def transaction(self,account_holder, reciver_account_name, amount):
     
        # for key, value in self.account_holders.items():
        match = False
        if reciver_account_name == self.account_holders[reciver_account_name].name:
            match = True
            account_holder.current_balance -= amount
            self.account_holders[reciver_account_name].current_balance += amount
            account_holder.transaction_history_personal.append('sending money')
            self.account_holders[reciver_account_name].transaction_history_personal.append('receiving Money')
        if match == False:
            print("Account does not exist")


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