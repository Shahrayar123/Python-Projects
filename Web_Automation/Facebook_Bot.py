from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Facebook:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.bot=webdriver.Chrome()
        
    def login(self):
        bot=self.bot
        bot.get("https://www.facebook.com/")
        time.sleep(5)
        email=bot.find_element_by_id("email")
        email.clear()
        email.send_keys(self.username)
        password=bot.find_element_by_id("pass")
        password.clear()
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)


load = Facebook('enter_email','enter_password')
load.login()
