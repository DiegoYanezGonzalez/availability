from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_form_submission():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=chrome_options)

    driver.get("http://127.0.0.1:5000")

    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "room")))
    driver.find_element(By.NAME, "room").send_keys("A")
    driver.find_element(By.NAME, "time").send_keys("10:00")
    driver.find_element(By.TAG_NAME, "form").submit()

    assert "Reserved successfully" in driver.page_source
    driver.quit()
