import time

from selenium import webdriver

class ChromeDriverWindows():

    def searchGoogle(self):
        driver = webdriver.Chrome(executable_path="C:\\Users\\wuoct\\Desktop\\TestingCourse\\chromedriver_win32\\chromedriver.exe")
        driver.get('https://www.google.com/?gws_rd=ssl')

        btn = driver.find_element_by_id('L2AGLb')
        btn.click()

        driver.maximize_window()

        searchInput = driver.find_element_by_name('q')
        searchInput.send_keys('some stuff')
        searchInput.submit()

        time.sleep(50)

#   id = L2AGLb


search = ChromeDriverWindows()

search.searchGoogle()
