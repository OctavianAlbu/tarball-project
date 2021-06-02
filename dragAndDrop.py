import time
import win32api

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from config.settings import *

driver = webdriver.Chrome(
    executable_path=CHROME_PATH)

class TestingDragAndDrop:

    def dragAndDrop(self):
        driver.maximize_window()
        driver.get("https://jqueryui.com/droppable/")
        driver.switch_to.frame(0)
        draggableElement = driver.find_element_by_id('draggable')
        dropzone = driver.find_element_by_id('droppable')
        action = ActionChains(driver)
        action.drag_and_drop(draggableElement, dropzone).perform()
        time.sleep(5)

test = TestingDragAndDrop()

test.dragAndDrop()

# driver.quit()