from selenium.webdriver.common.by import By

def add_cart(driver, item_id):
    try:
        driver.get("https://paypaymall.yahoo.co.jp/store/y-lohaco/item/{item_id}/".format(item_id=item_id))
        add_button = driver.find_element(By.ID,'CartButtonUltLog')
        add_button.click()
        return True
    except Exception as e:
        return False
