
import random
import sys
import sqlite3
random.seed()


conn = sqlite3.connect('card.s3db')
cur = conn.cursor()
# cur.execute("DROP TABLE card")
cur.execute("CREATE TABLE IF NOT EXISTS card(id INTEGER PRIMARY KEY,number TEXT,pin TEXT,balance INTEGER DEFAULT 0);")
conn.commit()


class Card:

    def __init__(self):
        self.card = ''
        self.pin = ''
        self.login_card = ''
        self.login_pin = ''
        self.row = []
        self.balance = 0
        self.receiver_balance = 0
        
    def create_account(self):
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

        self.login_card = input("Enter your card number:\n")
        self.login_pin = input("Enter your PIN:\n")

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

        '''elif not self.luhn_2(self.login_card):
            print('Probably you made a mistake in the card number. Please try again!')'''
            
    def success(self):
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
                print('\nEnter income:')
                amount = int(input())
                self.balance += amount
                cur.execute(f'UPDATE card SET balance = {self.balance} WHERE number = {self.login_card};')
                conn.commit()
                print('Income was added!')
            elif i == 3:
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

            elif i == 4:
                cur.execute(f"DELETE FROM card WHERE number = {self.login_card}")
                conn.commit()
                print('\nThe account has been closed!')
                break
            elif i == 5:
                print("\nYou have successfully log out!")
                break
            elif i == 0:
                print("\nBye!")
                conn.close()
                sys.exit()

    def luhn_2(self, num):
        num2 = num[:]
        num2 = num2[::-1]
        lst = [int(x) for x in num2]
        s1 = sum(lst[::2])
        for i in range(len(lst)):
            if i % 2 != 0:
                lst[i] = lst[i] * 2
        for i in range(len(lst)):
            if lst[i] > 9:
                lst[i] -= 9
        s2 = sum(lst[1:len(lst):2])

        if (s1 + s2) % 10 == 0:
            return True
        return False
                
    # Defining my luhn algorithm for creating a new card number
    def luhn(self):

        lst2 = [int(x) for x in self.card]
        lst3 = lst2[:]
        
        for i in range(len(lst3)):
            if i % 2 == 0:
                lst3[i] = lst3[i] * 2
            else:
                lst3[i] = lst3[i]
    
        for i in range(len(lst3)):
            if lst3[i] > 9:
                lst3[i] -= 9
            
        tot = sum(lst3)
        count_sum = 0
        while True:
            if (tot + count_sum) % 10 == 0:
                break
            else:
                count_sum += 1
                
        lst2.append(count_sum)
        self.card = (''.join(map(str, lst2)))
        
        return self.card
        
    def menu(self):
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
                

card = Card()
card.menu()