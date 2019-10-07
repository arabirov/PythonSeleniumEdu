from selenium import webdriver
from tests.common.constants import *
import time

driver = webdriver.Firefox(executable_path=FIREFOX_DRIVER_PATH, service_log_path=DRIVER_LOGS_PATH + "/geckodriver.log")

driver.implicitly_wait(1)
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()
driver.find_element_by_id("welcome").click()
driver.find_element_by_id("welcome").click()
driver.find_element_by_link_text("Logout").click()

time.sleep(2)
driver.close()
driver.quit()
print("Test completed")
