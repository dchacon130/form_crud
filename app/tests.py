from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Create your tests here.


try:
    chrome_options = Options()
    chrome_options.add_argument('--headless')

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    driver.get('http://127.0.0.1:9000/')
    welcome_message = driver.find_element(by=By.XPATH, value='/html[1]/body[1]/main[1]/h1[1]').text
    print(welcome_message)
    assert welcome_message == 'The install worked successfully! Congratulations!'
except Exception as ex:
    print('Error: ', ex)
finally:
    driver.quit()


