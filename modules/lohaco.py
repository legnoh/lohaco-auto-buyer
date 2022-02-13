from selenium.webdriver.common.by import By

def add_cart(driver, url):
    try:
        driver.get(url)
        add_button = driver.find_element(By.ID,'CartButtonUltLog')
        add_button.click()
        return True
    except Exception as e:
        return False
