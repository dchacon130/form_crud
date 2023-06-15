from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

# Create your tests here.


try:
    firefox_options = Options()
    firefox_options.add_argument('--headless')

    
    #Ubuntu
    geckodriver_path = '/usr/local/bin/geckodriver'

    driver = webdriver.Firefox(executable_path=geckodriver_path, options=firefox_options)

    driver.get('http://127.0.0.1:9000/')
    welcome_message = driver.find_element(by=By.XPATH, value='/html[1]/body[1]/main[1]/h1[1]').text
    print(welcome_message)
    assert welcome_message == 'The install worked successfully! Congratulations!'
except Exception as ex:
    print('Error: ', ex)
finally:
    driver.quit()


