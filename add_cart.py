import os
from selenium import webdriver
import chromedriver_binary
import modules.yahoo as yahoo
import modules.lohaco as lohaco

yahoo_id = os.environ.get('YAHOO_ID')
yahoo_password = os.environ.get('YAHOO_PASSWORD')
driver = webdriver.Chrome()

# login
yahoo.login(driver, yahoo_id, yahoo_password)

# add cart
item_id =  os.environ.get('LOHACO_ITEM_ID')
lohaco.add_cart(driver, item_id)

driver.quit()
