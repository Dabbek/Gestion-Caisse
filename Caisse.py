from selenium.webdriver.chrome.service import Service
import unittest
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
class Ajout_Facteur(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)
    def test_search(self):
        driver = self.driver
        driver.get("http://41.226.182.130:3002/login")        
        username = driver.find_element(By.XPATH, "//input[@id='login']")   
        username.send_keys("Hazar")
        password = driver.find_element(By.ID, "loginPassword")
        password.send_keys("hazar1234")
        login_button = driver.find_element(By.XPATH, "//button[normalize-space()='Se Connecter']")
        login_button.click()
        Section_Caisse_button = driver.find_element(By.XPATH, "//a[@href='caisse']//div[@class='d-flex align-items-center']")
        Section_Caisse_button.click()
        Ajout_Caisse_button = driver.find_element(By.XPATH, "//span[@class='text']")
        Ajout_Caisse_button.click()
        Ajout_NC = driver.find_element(By.XPATH, "//input[@id='caisse']")
        Ajout_NC.send_keys("TEST1")
        Ajout_S = driver.find_element(By.XPATH, "//input[@id='solde']")
        Ajout_S.send_keys("1000")
        Ajouter_button = driver.find_element(By.XPATH, "//button[normalize-space()='Ajouter']")
        Ajouter_button.click()

    # # def tearDown(self):
    # # def tearDown(self):
    #     self.driver.close()
if __name__ == "__main__":
    unittest.main()