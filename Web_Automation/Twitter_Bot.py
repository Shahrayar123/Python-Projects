from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Twitter():
  def __init__(self,username,password):
    self.username = username
    self.password = password
    self.bot = webdriver.Chrome()
  
  def login(self):
    bot = self.bot
    bot.get('https://twitter.com/login')
    time.sleep(3)
    email = bot.find_element_by_name('session[username_or_email]')
    email.send_keys(Keys.RETURN)
    password = bot.find_element_by_name('seccion[password]')
    password.send_keys(self.password)
    time.sleep(3)
    password.send_keys(Keys.RETURN)
  

load = Twitter('enter_email','enter_password')
load.login()
