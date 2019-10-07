import unittest
from selenium import webdriver
from tests.common.constants import *


class Init(unittest.TestCase):
    def setUp(self):
        self._driver = webdriver.Firefox(executable_path=FIREFOX_DRIVER_PATH, service_log_path=DRIVER_LOGS_PATH + "/geckodriver.log")

    def tearDown(self):
        self._driver.close()

