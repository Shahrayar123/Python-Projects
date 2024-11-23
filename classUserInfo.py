class UserInfo:
    def __init__(self, username, password, email):
        self.username=username
        self.password=password
        self.email=email
user1 = UserInfo("Mak", "123456", "mak@example.com")
print(user1.username)
print(user1.email)
        