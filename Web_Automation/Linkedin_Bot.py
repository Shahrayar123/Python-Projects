from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Linkedin:
  def __init(self,username , password):
    self.username = username
    self.password = password
    self.bot = webdriver.Chrome()
  
  def login(self):
    bot = self.bot
    bot.get("https://www.linkedin.com/login")
    time.sleep(4)
    email = bot.find_element_by_id('username')
    email.send_keys(self.username)
    password = bot.find_element_by_id('password')
    password.send_keys(self.password)
    time.sleep(4)
    password.send_keys(Keys.RETURN)


load = Linkedin('enter_email','enter_password')
load.login()
