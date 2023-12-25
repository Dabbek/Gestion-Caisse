from selenium.webdriver.chrome.service import Service
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Login(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)

    def test_search(self):
        driver = self.driver
        driver.get("http://41.226.182.130:3002/login")
        
        username = driver.find_element(By.ID, "login")   
        username.send_keys("Hazar")

        password = driver.find_element(By.ID, "loginPassword")
        password.send_keys("hazar1234")
        
        login_button = driver.find_element(By.XPATH, "//button[normalize-space()='Se Connecter']")
        login_button.click()
        current_url = driver.current_url
        expected_url = "http://41.226.182.130:3002/home"

        if current_url == expected_url:
            with open('rapport .txt', 'w') as file:
                file.write("Le résultat obtenu de test 1 correspond au résultat attendu.")
        else :
            with open('rapport .txt', 'w') as file:
                file.write("Le résultat obtenu de test 1 ne correspond pas au résultat attendu.")
        time.sleep(5)
    def tearDown(self):
        self.driver.close()
if __name__ == "__main__":
    unittest.main()