from selenium import webdriver # type: ignore
from selenium.webdriver.chrome.options import Options # type: ignore

def test_form_submission():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", options=chrome_options)
    driver.get("http://localhost:5000")

    room_input = driver.find_element("name", "room")
    time_input = driver.find_element("name", "time")
    room_input.send_keys("A")
    time_input.send_keys("10:00")

    submit_button = driver.find_element("tag name", "button")
    submit_button.click()
    driver.quit()