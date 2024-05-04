from abc import ABC

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

        




