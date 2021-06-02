import time
import win32api

from selenium import webdriver

from selenium.webdriver.common.by import By

from config.settings import *

driver = webdriver.Chrome(
    executable_path=CHROME_PATH)

class TestingRadioButton:

    def selectElement(self, type):
        arr = driver.find_elements_by_xpath('//input[@type='+'"'+type+'"'+']')
        for el in arr:
            if el.is_selected():
                print(el.get_attribute("value") + 'is selected ')
            else:
                el.click()
                print(el.get_attribute("value") + 'is selected ')
                time.sleep(1)

    def radioButton(self):
        driver.get("http://demo.guru99.com/test/radio.html")
        self.selectElement('radio')


    def checkbox(self):
        driver.get("http://demo.guru99.com/test/radio.html")
        self.selectElement('checkbox')


test = TestingRadioButton()

test.checkbox()

# driver.quit()