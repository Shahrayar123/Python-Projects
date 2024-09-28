import random
import sys
import sqlite3

# Set the random seed for reproducibility
random.seed()

# Connect to SQLite database
conn = sqlite3.connect('card.s3db')
cur = conn.cursor()

# Create the 'card' table if it doesn't exist
cur.execute("CREATE TABLE IF NOT EXISTS card(id INTEGER PRIMARY KEY,number TEXT,pin TEXT,balance INTEGER DEFAULT 0);")
conn.commit()

class Card:
    """
    A class representing a card in a banking system.
    
    This class handles account creation, login, and various banking operations.
    """

    def __init__(self):
        """Initialize Card object with default values."""
        self.card = ''
        self.pin = ''
        self.login_card = ''
        self.login_pin = ''
        self.row = []
        self.balance = 0
        self.receiver_balance = 0
        
    def create_account(self):
        """Create a new account with a unique card number and PIN."""
        print("Your card has been created")
        print("Your card number:")
        self.card = '400000' + str(random.randint(100000000, 999999999)) 
        print(self.luhn())
        print("Your card PIN:")
        self.pin = str(random.randint(1000, 9999))
        print(self.pin)
        cur.execute(f"""INSERT INTO card (number, pin) VALUES ({self.card}, {self.pin});""")
        conn.commit()
        
    def log_in(self):
        """Handle user login process."""
        self.login_card = input("Enter your card number:\n")
        self.login_pin = input("Enter your PIN:\n")

        # Verify login credentials
        cur.execute(f"""SELECT
                            id,
                            number,
                            pin,
                            balance
                        FROM 
                            card
                        WHERE
                            number = {self.login_card}
                            AND pin = {self.login_pin}
                        ;""")

        self.row = cur.fetchone()
        if self.row:
            self.balance = self.row[3]
            print('\nYou have successfully logged in')
            self.success()
        else:
            print("wrong card number or pin")
            
    def success(self):
        """Handle successful login and provide menu options."""
        while True:
            print("""\n1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit""")
            i = int(input())
            if i == 1:
                print('\nBalance: ', self.balance)
                print()
            elif i == 2:
                self.add_income()
            elif i == 3:
                self.do_transfer()
            elif i == 4:
                self.close_account()
                break
            elif i == 5:
                print("\nYou have successfully log out!")
                break
            elif i == 0:
                print("\nBye!")
                conn.close()
                sys.exit()

    def add_income(self):
        """Add income to the account."""
        print('\nEnter income:')
        amount = int(input())
        self.balance += amount
        cur.execute(f'UPDATE card SET balance = {self.balance} WHERE number = {self.login_card};')
        conn.commit()
        print('Income was added!')

    def do_transfer(self):
        """Handle money transfer between accounts."""
        print('\nTransfer\nEnter card number:')
        receiver_card = input()
        cur.execute(f'SELECT id, number,pin,balance FROM card WHERE number = {receiver_card};')

        if not self.luhn_2(receiver_card):
            print('Probably you made a mistake in the card number. Please try again!')
        elif not cur.fetchone():
            print('Such a card does not exist.')
        else:
            transfer = int(input("Enter how much money you want to transfer:\n"))
            if transfer > self.balance:
                print("Not enough money!")
            else:
                self.balance -= transfer
                cur.execute(f'UPDATE card SET balance = {self.balance} WHERE number = {self.login_card};')
                self.receiver_balance += transfer
                cur.execute(f'UPDATE card SET balance = {self.receiver_balance} WHERE number = {receiver_card};')
                cur.execute(f'SELECT * FROM card WHERE number = {self.login_card}')
                print(cur.fetchone())
                print("Success!")
                conn.commit()

    def close_account(self):
        """Close the current account."""
        cur.execute(f"DELETE FROM card WHERE number = {self.login_card}")
        conn.commit()
        print('\nThe account has been closed!')

    def luhn_2(self, num):
        """
        Validate card number using Luhn algorithm.
        
        Args:
            num (str): Card number to validate.
        
        Returns:
            bool: True if card number is valid, False otherwise.
        """
        num2 = num[::-1]
        lst = [int(x) for x in num2]
        s1 = sum(lst[::2])
        for i in range(1, len(lst), 2):
            lst[i] = lst[i] * 2
            if lst[i] > 9:
                lst[i] -= 9
        s2 = sum(lst[1::2])

        return (s1 + s2) % 10 == 0
                
    def luhn(self):
        """
        Generate a valid card number using Luhn algorithm.
        
        Returns:
            str: Valid card number.
        """
        lst2 = [int(x) for x in self.card]
        lst3 = lst2[:]
        
        for i in range(0, len(lst3), 2):
            lst3[i] *= 2
    
        lst3 = [x - 9 if x > 9 else x for x in lst3]
            
        tot = sum(lst3)
        count_sum = (10 - tot % 10) % 10
                
        lst2.append(count_sum)
        self.card = ''.join(map(str, lst2))
        
        return self.card
        
    def menu(self):
        """Display main menu and handle user choices."""
        while True:
            print("""\n1. Create an account
2. Log into account
0. Exit""")
            i = int(input())
            if i == 1:
                self.create_account()
            elif i == 2:
                self.log_in()
            elif i == 0:
                conn.close()
                print("\nBye!")
                break
            else:
                print("Invalid input")
                

# Create a Card object and start the program
card = Card()
card.menu()
