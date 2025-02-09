import unittest
from unittest.mock import patch, MagicMock
import sqlite3
from banking import Card, CardRepository, LuhnCardNumberGenerator, RandomPinGenerator, LuhnCardNumberValidator, CreditCardFactory

class TestCard(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(':memory:')
        self.repository = CardRepository(self.conn)
        self.number_generator = LuhnCardNumberGenerator()
        self.pin_generator = RandomPinGenerator()
        self.number_validator = LuhnCardNumberValidator()
        self.factory = CreditCardFactory(self.repository, self.number_generator, self.pin_generator, self.number_validator)
        self.card = Card(self.repository, self.factory)

    def tearDown(self):
        self.conn.close()

    def test_create_account(self):
        card_number, pin = self.card.create_account()
        self.assertEqual(len(card_number), 16)
        self.assertEqual(len(pin), 4)
        self.assertTrue(self.number_validator.validate(card_number))

    def test_log_in_success(self):
        card_number, pin = '1234567890123456', '1234'
        self.repository.create_card(card_number, pin)
        self.assertTrue(self.card.log_in(card_number, pin))

    def test_log_in_failure_wrong_pin(self):
        card_number, pin = '1234567890123456', '1234'
        self.repository.create_card(card_number, pin)
        self.assertFalse(self.card.log_in(card_number, '4321'))

    def test_log_in_failure_wrong_card(self):
        self.assertFalse(self.card.log_in('1234567890123456', '1234'))

    def test_get_balance(self):
        card_number, pin = '1234567890123456', '1234'
        self.repository.create_card(card_number, pin)
        self.repository.update_balance(card_number, 1000)
        self.card.log_in(card_number, pin)
        self.assertEqual(self.card.get_balance(), 1000)

    def test_add_income(self):
        card_number, pin = '1234567890123456', '1234'
        self.repository.create_card(card_number, pin)
        self.card.log_in(card_number, pin)
        self.card.add_income(500)
        self.assertEqual(self.card.get_balance(), 500)

    def test_do_transfer_success(self):
        sender_card, sender_pin = self.card.create_account()
        receiver_card, receiver_pin = self.card.create_account()
        self.repository.update_balance(sender_card, 1000)
        self.card.log_in(sender_card, sender_pin)
        self.assertEqual(self.card.do_transfer(receiver_card, 300), "Success!")
        self.assertEqual(self.card.get_balance(), 700)
        receiver_row = self.repository.get_card(receiver_card)
        self.assertEqual(receiver_row[3], 300)

    def test_do_transfer_invalid_card(self):
        sender_card, sender_pin = self.card.create_account()
        self.repository.update_balance(sender_card, 1000)
        self.card.log_in(sender_card, sender_pin)
        self.assertEqual(self.card.do_transfer('9876543210987654', 300), "Probably you made a mistake in the card number. Please try again!")

    def test_do_transfer_not_enough_money(self):
        sender_card, sender_pin = self.card.create_account()
        receiver_card, _ = self.card.create_account()
        self.card.log_in(sender_card, sender_pin)
        self.assertEqual(self.card.do_transfer(receiver_card, 300), "Not enough money!")

    def test_close_account(self):
        card_number, pin = '1234567890123456', '1234'
        self.repository.create_card(card_number, pin)
        self.card.log_in(card_number, pin)
        self.card.close_account()
        self.assertFalse(self.repository.check_card_exists(card_number))

if __name__ == '__main__':
    unittest.main()