import random
import abc
import sqlite3

# Database repository
class CardRepository:
    def __init__(self, connection):
        self.conn = connection
        self.cur = connection.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS card(id INTEGER PRIMARY KEY, number TEXT, pin TEXT, balance INTEGER DEFAULT 0);")
        self.conn.commit()

    def create_card(self, number, pin):
        self.cur.execute(f"""INSERT INTO card (number, pin) VALUES ('{number}', '{pin}');""")
        self.conn.commit()

    def get_card(self, number):
        self.cur.execute(f"""SELECT id, number, pin, balance FROM card WHERE number = '{number}';""")
        return self.cur.fetchone()

    def update_balance(self, number, balance):
        self.cur.execute(f'UPDATE card SET balance = {balance} WHERE number = {number};')
        self.conn.commit()

    def delete_card(self, number):
        self.cur.execute(f"DELETE FROM card WHERE number = '{number}'")
        self.conn.commit()

    def check_card_exists(self, number):
        self.cur.execute(f'SELECT id, number, pin, balance FROM card WHERE number = "{number}";')
        return bool(self.cur.fetchone())

# Strategies
class CardNumberGenerator(abc.ABC):
    @abc.abstractmethod
    def generate(self):
        pass

class LuhnCardNumberGenerator(CardNumberGenerator):
    def generate(self):
        card_number = '400000' + str(random.randint(100000000, 999999999))
        return self.luhn(card_number)

    def luhn(self, num):
        lst2 = [int(x) for x in num]
        lst3 = lst2[:]
        for i in range(len(lst3)):
            if i % 2 == 0:
                lst3[i] = lst3[i] * 2
        for i in range(len(lst3)):
            if lst3[i] > 9:
                lst3[i] -= 9
        tot = sum(lst3)
        count_sum = 0
        while (tot + count_sum) % 10 != 0:
            count_sum += 1
        lst2.append(count_sum)
        return ''.join(map(str, lst2))

class PinGenerator(abc.ABC):
    @abc.abstractmethod
    def generate(self):
        pass

class RandomPinGenerator(PinGenerator):
    def generate(self):
        return str(random.randint(1000, 9999))

class CardNumberValidator(abc.ABC):
    @abc.abstractmethod
    def validate(self, number):
        pass

class LuhnCardNumberValidator(CardNumberValidator):
    def validate(self, num):
        num2 = num[::-1]
        lst = [int(x) for x in num2]
        s1 = sum(lst[::2])
        for i in range(len(lst)):
            if i % 2 != 0:
                lst[i] = lst[i] * 2
        for i in range(len(lst)):
            if lst[i] > 9:
                lst[i] -= 9
        s2 = sum(lst[1:len(lst):2])
        return (s1 + s2) % 10 == 0

# Card Factory
class CardFactory(abc.ABC):
    @abc.abstractmethod
    def create_card(self):
        pass

class CreditCardFactory(CardFactory):
    def __init__(self, repository, number_generator, pin_generator, number_validator):
        self.repository = repository
        self.number_generator = number_generator
        self.pin_generator = pin_generator
        self.number_validator = number_validator

    def create_card(self):
        card_number = self.number_generator.generate()
        pin = self.pin_generator.generate()
        self.repository.create_card(card_number, pin)
        return card_number, pin

# Card
class Card:
    def __init__(self, repository, factory):
        self.repository = repository
        self.factory = factory
        self.login_card = ''
        self.login_pin = ''
        self.row = []
        self.balance = 0

    def create_account(self):
        return self.factory.create_card()

    def log_in(self, card_number, pin):
        self.login_card = card_number
        self.login_pin = pin
        self.row = self.repository.get_card(self.login_card)
        if self.row:
            if self.row[2] == pin:  # Check if the PIN matches the card number
                self.balance = self.row[3]
                return True
            else:
                return False
        else:
            return False

    def get_balance(self):
        return self.balance

    def add_income(self, income):
        self.balance += income
        self.repository.update_balance(self.login_card, self.balance)

    def do_transfer(self, receiver_card, transfer_amount):
        if not self.factory.number_validator.validate(receiver_card):
            return "Probably you made a mistake in the card number. Please try again!"
        if not self.repository.check_card_exists(receiver_card):
            return "Such a card does not exist."
        if transfer_amount > self.balance:
            return "Not enough money!"
        self.balance -= transfer_amount
        self.repository.update_balance(self.login_card, self.balance)
        receiver_row = self.repository.get_card(receiver_card)
        receiver_balance = receiver_row[3] + transfer_amount
        self.repository.update_balance(receiver_card, receiver_balance)
        return "Success!"

    def close_account(self):
        self.repository.delete_card(self.login_card)



if __name__=='__main__':
    # Example usage
    conn = sqlite3.connect('card.s3db')
    repository = CardRepository(conn)
    number_generator = LuhnCardNumberGenerator()
    pin_generator = RandomPinGenerator()
    number_validator = LuhnCardNumberValidator()
    factory = CreditCardFactory(repository, number_generator, pin_generator, number_validator)
    card = Card(repository, factory)

    # Create an account
    card_number, pin = card.create_account()
    print(f"Your card has been created\nYour card number:\n{card_number}\nYour card PIN:\n{pin}")
    receiver_card_number, receiver_pin = card.create_account()
    print(f"Your card has been created\nYour card number:\n{receiver_card_number}\nYour card PIN:\n{receiver_pin}")

    # Log in
    card.log_in(card_number, pin)
    card.log_in(receiver_card_number, receiver_pin)

    # Add income
    card.add_income(1000)

    # Transfer money
    print(card.do_transfer(receiver_card_number, 300))

    # Get balance
    print(f"Your balance: {card.get_balance()}")

    # Close account
    card.close_account()

    conn.close()
