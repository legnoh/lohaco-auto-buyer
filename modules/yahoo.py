from selenium.webdriver.common.by import By

def login(driver, id, password):
    driver.get("https://login.yahoo.co.jp/config/login")
    driver.implicitly_wait(10);
    email_box = driver.find_element(By.NAME, 'login')
    email_box.send_keys(id)
    next_button = driver.find_element(By.NAME, 'btnNext')
    next_button.click()
    password_box = driver.find_element(By.NAME, 'passwd')
    password_box.send_keys(password)
    email_box.submit()
