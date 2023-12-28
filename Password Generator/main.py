import random

# types of arrays to include in password criteria
lowercase = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
    "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]

uppercase = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
    "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]

numeric = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

specialchar = [
    "!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/",
    "\\", ":", ";", "<", ">", "=", "?", "@", "[", "]", "^", "_", "`", "{", "}",
    "|", "~"
]


def generate_password():
  # prompt to determine length of the password generated
  password_length = int(
      input("Choose a password length between 8 and 128 characters: "))
  if password_length < 8 or password_length > 128:
    return "Choose a number between 8 and 128 characters."

  lowercase_question = input(
      "Do you want your password to include lowercase letters? (y/n): ").lower(
      ) == 'y'
  uppercase_question = input(
      "Do you want your password to include uppercase letters? (y/n): ").lower(
      ) == 'y'
  numeric_question = input(
      "Do you want your password to include numbers? (y/n): ").lower() == 'y'
  specialchar_question = input(
      "Do you want your password to include special characters? (y/n): "
  ).lower() == 'y'

  # password must have at least 1 array of criteria
  if not (lowercase_question or uppercase_question or numeric_question
          or specialchar_question):
    return "Select at least one character type."

  password_final = []
  if lowercase_question:
    password_final += lowercase
  if uppercase_question:
    password_final += uppercase
  if numeric_question:
    password_final += numeric
  if specialchar_question:
    password_final += specialchar

# complete_password will be a string
  complete_password = ""
# this loop will take the password criteria selected generate a random password
  for _ in range(password_length):
    total = random.choice(password_final)
    complete_password += total

  return 'Your Password is: ' + complete_password


# print function
print(generate_password())