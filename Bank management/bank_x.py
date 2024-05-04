from users import User
from datetime import datetime

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
    
    
        
                

    

        

