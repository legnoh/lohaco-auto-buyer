import os
from selenium import webdriver
import chromedriver_binary
import modules.yahoo as yahoo
import modules.lohaco as lohaco

print("Initializing...")
yahoo_id = os.environ.get('YAHOO_ID')
yahoo_password = os.environ.get('YAHOO_PASSWORD')

print("Opening Browser...")
driver = webdriver.Chrome()

# login
print("Logging in...")
yahoo.login(driver, yahoo_id, yahoo_password)

# add cart
print("Adding to cart...")
item_id =  os.environ.get('LOHACO_ITEM_ID')
lohaco.add_cart(driver, item_id)

print("Closing Browser...")
driver.quit()

print("Well Done!")
