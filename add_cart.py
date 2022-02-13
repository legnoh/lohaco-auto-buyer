import os,yaml
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

# read yml file
with open('config/items.yml', 'r') as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)

# serch product
candidate_items = None
genre_name =  os.environ.get('GENRE_NAME')
product_name =  os.environ.get('ITEM_NAME')
print("product: {product_name}".format(product_name=product_name))
for item in config['genres'][genre_name]['items']:
    if product_name == item['product_name']:
        candidate_items = item['candidates']
        break
if candidate_items == None:
    print("ERROR: Product not found.")
    exit(1)

# add cart
print("Adding to cart...")
is_success = False
for candidate in candidate_items:
    if lohaco.add_cart(driver, candidate['url']):
        print("SUCCESS: Added to cart - {item_name}".format(item_name=candidate['name']))
        is_success = True
        break
    else:
        print("WARN: {item_name} is not sold...".format(item_name=candidate['name']))

if is_success == False:
    print("ERROR: Failed to add all candidates to cart.")
    print("Closing Browser...")
    driver.quit()
    exit(1)

print("Closing Browser...")
driver.quit()

print("SUCCESS: Well Done!")
