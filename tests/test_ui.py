from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:5000") 
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "room")))
    driver.find_element(By.NAME, "room").send_keys("A")
    driver.find_element(By.NAME, "time").send_keys("10:00")
    driver.find_element(By.TAG_NAME, "form").submit()


    assert driver.find_element(By.NAME, "room").is_displayed()

    driver.quit()
