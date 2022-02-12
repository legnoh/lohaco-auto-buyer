from selenium.webdriver.common.by import By

def add_cart(driver, item_id):
    try:
        driver.get("https://paypaymall.yahoo.co.jp/store/y-lohaco/item/{item_id}/".format(item_id=item_id))
        add_button = driver.find_element(By.ID,'CartButtonUltLog')
        add_button.click()
    except Exception as e:
        print("WARN: {item_id} is not found...".format(item_id=item_id))
