import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import random
import string

letters = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
password = "password"

url = "https://itera-qa.azurewebsites.net"
driverInstall = ChromeDriverManager().install()


class TestRegister(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(
            options=options, service=Service(driverInstall))
        self.browser.maximize_window()

    def test_a_success_register(self):
        # stepds
        browser = self.browser  # buka web browser
        browser.get(url + "/UserRegister/NewUser")
        time.sleep(3)

        browser.find_element(By.ID, "FirstName").send_keys(
            letters)
        time.sleep(1)
        browser.find_element(By.ID, "Surname").send_keys(
            letters)
        time.sleep(1)
        browser.find_element(By.ID, "Username").send_keys(
            letters)
        time.sleep(1)
        browser.find_element(By.ID, "Password").send_keys(
            password)
        time.sleep(1)
        browser.find_element(By.ID, "ConfirmPassword").send_keys(
            password)
        time.sleep(1)
        browser.find_element(By.ID, "submit").click()  # klik tombol sign in
        time.sleep(1)

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()
