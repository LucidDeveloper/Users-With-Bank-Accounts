# Import module from <folder name> import <class name>
#Import User class from user.py module

from user import User

'''
@ author
Gianni M. Javier
'''

# Create 3 instances of the User class which have been updated to associate with the BankAccount class
gianni = User("Gianni","Javier")    # instance of the class aka an object
eya = User("Andrea","Avila")
bruno = User("Bruno", "Avila")

# All User Instances are Instantiated with a
# savings account balance of $50000 with a 5% interest rate
# and a checking account balance of $20000 with a 2% interest rate

# first user makes two deposits and one withdrawal, specifying from which account at each transaction, and then displays the user balance
gianni.make_deposit('savings',500).make_deposit('checking',10000).make_withdrawal('checking', 400).display_user_balance()

# second user makes one deposit and two withdrawals, specifying from which account at each transaction, and then displays the user balance
eya.make_deposit('checking',1000).make_withdrawal('savings',250).make_withdrawal('savings',250).display_user_balance()

# third user makes two deposits and two withdrawals, specifying from which account at each transaction, and then displays the user balance
bruno.make_deposit('checking',1000).make_withdrawal('checking',500).make_deposit('savings',1000).make_withdrawal('savings',500).display_user_balance()

# first user transfers money to third user, and then to second user, specifying from which account at each transaction, and then displays account
gianni.transfer_money('checking',eya,'checking',500).transfer_money('checking',bruno,'checking', 500).display_user_balance()
eya.display_user_balance()
bruno.display_user_balance()