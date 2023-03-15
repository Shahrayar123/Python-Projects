import string
import secrets
length=int(input("Enter the length of the required password:"))
alphabet = string.ascii_letters + string.digits + string.punctuation
password = ''.join(secrets.choice(alphabet) for i in range(length))
print("Here is your password:",password)