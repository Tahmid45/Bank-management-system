from users import User
from datetime import datetime

class Bank:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.account_holders = {}
        self.total_balance = 0
        self.total_loan = 0
        self.transaction_history_bank = {}    #{'name' : obect()}
        self.bankrupt = False
        self.loan = True
        self.time_date = None

    def generate_account(self,account_holder):
        account_id = f"{self.name}-{len(self.account_holders)}"
        account_holder.account_number = account_id
        self.account_holders[account_holder.name] = account_holder
    
    def delete_account(self, name):
        for name in self.account_holders.keys():
            self.account_holders.pop(name)

    def see_all_users(self):
        print("ALL users are Here")
        print(f"name\t phone \temail" )
        for key, account in self.account_holders.items():
            if key != 'admin':
                
                print(f"{account.name}\t {account.phone} \t{account.email}" )
    
    def update_balance(self, amount):
        self.total_balance += amount
    def update_balance_for_withdraW(self, amount):
        self.total_balance -= amount

    def loan_feature_on(self):
        self.loan = True
    
    def loan_feature_off(self):
        self.loan = False
        
    def take_loan(self, name, amount):
        if self.loan == True:
            self.total_loan += amount
            self.total_balance -= amount
            

    def transaction(self,account_holder, reciver_account_name, amount):
        account_holder.current_balance -= amount
        self.account_holders[reciver_account_name].current_balance += amount
        account_holder.transaction_history[account_holder.name] = [datetime.now(), 'sending money']
        self.account_holders[reciver_account_name].transaction_history = [datetime.now(), 'receiving Money']
        

    

        

