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
        username = driver.find_element(By.ID, "login")   
        username.send_keys("Hazar")
        password = driver.find_element(By.ID, "loginPassword")
        password.send_keys("hazar1234")
        login_button = driver.find_element(By.XPATH, "//button[normalize-space()='Se Connecter']")
        login_button.click()
        Acteurs_button = driver.find_element(By.XPATH," //a[@href='client']//div[@class='d-flex align-items-center']//div[@class='text-center flex-grow-1 mb-5 mt-5']")
        Acteurs_button.click()
        AjoutF_button = driver.find_element(By.XPATH,"//span[@class='text'] ")
        AjoutF_button.click()
        AjouN = driver.find_element(By.ID, "company")   
        AjouN.send_keys("hanen")
        AjouA = driver.find_element(By.ID, "title")   
        AjouA.send_keys("Gabes")
        Ajout_Num = driver.find_element(By.ID, "numtel")   
        Ajout_Num.send_keys("58154536")  
        dropdown_element = driver.find_element(By.XPATH, "//select[@class='form-control ng-untouched ng-pristine ng-invalid']")
        dropdown = Select(dropdown_element)
        option_text = 'Personne'   
        dropdown.select_by_visible_text(option_text)
        Ajout_button = driver.find_element (By.XPATH,"//button[normalize-space()='Ajouter']")
        Ajout_button.click()
        current_url = driver.current_url
        expected_url = "http://41.226.182.130:3002/client"
        if current_url == expected_url:
            with open('rapport .txt', 'w') as file:
                file.write("Le résultat obtenu de test 2 correspond au résultat attendu.")
        else :
            with open('rapport .txt', 'w') as file:
                file.write("Le résultat obtenu de test 2 ne correspond pas au résultat attendu.")
    # def tearDown(self):
    #     self.driver.close()
if __name__ == "__main__":
    unittest.main()