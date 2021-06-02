import time
import win32api

from selenium import webdriver

# BOTH INPUTS HAVE THE RIGHT VALUES - logs u in
from selenium.webdriver.common.by import By

from config.settings import USERNAME, PASSWORD, CHROME_PATH, URL

driver = webdriver.Chrome(
    executable_path=CHROME_PATH)

#'mngr327705'
#'enuvEdU'

class TestingLogin():

    def loginTemplate(self, username, passcode):

        driver.get(URL)

        user = driver.find_element_by_xpath("//input[@name='uid']")
        user.send_keys(username)
        password = driver.find_element_by_name('password')
        password.send_keys(passcode)
        btnLogin = driver.find_element_by_name('btnLogin')
        btnLogin.click()

    def LoginNotOK(self, username, passcode, testcase):

        self.loginTemplate(username, passcode)
         # for when u expect for a login to fail(but test pass)
        try:
            actualTitle = driver.title
            if (actualTitle == 'Guru99 Bank Manager HomePage'):
                print('TEST CASE ' + testcase + ' FAILED')
        except:
            print('TEST CASE ' + testcase + ' PASSED')

        time.sleep(5)

    def LoginOK(self, username, passcode, testcase):

        self.loginTemplate(username, passcode)

        # driver.get(URL)
        # # user = driver.find_element_by_name('uid')
        # # user = driver.find_element(By.NAME, 'uid')
        # user = driver.find_element_by_xpath("//input[@name='uid']")
        # # user = driver.find_element(By.XPATH, "//input[contains(@name, 'uid')]")  REGEX
        # user.send_keys(username)
        # password = driver.find_element_by_name('password')
        # password.send_keys(passcode)
        # btnLogin = driver.find_element_by_name('btnLogin')
        # btnLogin.click()

        # for when u expect a login to pass
        try:
            actualTitle = driver.title
            print(actualTitle)
            if (actualTitle == 'Guru99 Bank Manager HomePage'):
                print('TEST CASE ' + testcase + ' PASSED')
        except:
            print('TEST CASE '  + testcase + ' FAILED')


test = TestingLogin()

test.LoginNotOK(USERNAME, PASSWORD, 'user and password ok')
test.LoginOK(USERNAME, PASSWORD, 'user and password ok')
test.LoginNotOK('userNOTok', PASSWORD, 'user not ok but password ok')
test.LoginNotOK(USERNAME, 'passwordNOTok', 'user ok but password not ok')
test.LoginNotOK('', PASSWORD, 'user empty')
test.LoginNotOK(USERNAME, '', 'password empty')

driver.quit()