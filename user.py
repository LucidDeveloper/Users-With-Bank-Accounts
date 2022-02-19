# Import module keywords from <folder name> import <class name>
# Import BankAccount class from bank_account.py module

from bank_account import BankAccount

'''
@ author 
Gianni M. Javier
'''

'''
Update the User class __init__ method to associate with BankAccount class from the bank_account module 
in order to Instantiate an Instance of the BankAccount class in order to associate with 
the Instantiation of the Instance of the User class
'''

# Create a file with the User class, including the __init__ and make_deposit methods
# Class/Bllueprint for Object/Instance of a Class
class User:
    def __init__(self, first_name,last_name): # Special Method defined in Python, works as Class Constructor
        self.first_name = first_name # Attributes created with every Instantiation of an Object/Instance of a class
        self.last_name = last_name
        self.checking = BankAccount(interest_rate = 0.02, account_balance = 20000) # Instantiate instance of BankAccount class with default interest rate and account balance
        self.savings = BankAccount(interest_rate = 0.05, account_balance = 50000 ) # Instantiate instance of BankAccount class with default interest rate and account balance

    '''
Update the User class make_deposit method to associcate with the Instantiation of the 
Instance of the BankAccount class from the bank_account module
'''

# Make_deposit(self, amount) - have this method increase the user's balance by the amount specified
    def make_deposit(self,account_type,amount):
        if account_type == 'savings':
            self.savings.account_balance += amount 
        else:
            self.checking.account_balance += amount
        return self

    '''
Update the User class make_withdrawal method to associcate with the Instantiation of the 
Instance of the BankAccount class from the bank_account module.
(For reference, User class, before association, and BankAccount class are found in the repositories named User and Bank Account repectively.)
'''

# Add a make_withdrawal method to the User class      
# Make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
    def make_withdrawal(self,account_type,amount):
        if account_type == 'savings':
            self.savings.account_balance -= amount
        else:
            self.checking.account_balance -= amount
        return self

    '''
Update the User class display_user_balance method to associcate with the Instantiation of the 
Instance of the BankAccount class from the bank_account module
'''

# Add a display_user_balance method to the User class
# Display_user_balance(self) - have this method print the user's name and account balance to the terminal
# eg. "User: Guido van Rossum, Balance: $150
    def display_user_balance(self):
        print(f'\nUser: {self.first_name} {self.last_name}, Checking Balance: ${self.checking.account_balance}')
        print(f'User: {self.first_name} {self.last_name}, Savings Balance: ${self.savings.account_balance}\n')
        return self

    '''
Update the User class transfer_money method to associcate with the Instantiation of the 
Instance of the BankAccount class from the bank_account module
'''

# BONUS: transfer_money(self, other_user, amount) - 
# have this method decrease the user's balance by the amount and 
# add that amount to other other_user's balance
    def transfer_money(self,self_account_type,other_user,other_user_account_type,amount):
        if self_account_type == 'savings' and other_user_account_type == 'savings':
            self.savings.account_balance -= amount
            other_user.savings.account_balance += amount
        elif self_account_type == 'savings' and other_user_account_type == 'checking':
            self.savings.account_balance -= amount
            other_user.checking.account_balance += amount
        elif self_account_type == 'checking' and other_user_account_type == 'savings':
            self.checking.account_balance -= amount
            other_user.savings.account_balance += amount
        else:
            self.checking.account_balance -= amount
            other_user.checking.account_balance += amount
        return self
