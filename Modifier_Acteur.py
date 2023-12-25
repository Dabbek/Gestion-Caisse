from selenium.webdriver.chrome.service import Service
import unittest
from selenium.webdriver.support.select import Select
from selenium import webdriver
import time
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
        #login   
        username = driver.find_element(By.ID, "login")   
        username.send_keys("Hazar")
        #password
        password = driver.find_element(By.ID, "loginPassword")
        password.send_keys("hazar1234")
        login_button = driver.find_element(By.XPATH, "//button[normalize-space()='Se Connecter']")
        login_button.click()
        #acces Section Acteurs_Financiére
        Acteurs_button = driver.find_element(By.XPATH," //a[@href='client']//div[@class='d-flex align-items-center']//div[@class='text-center flex-grow-1 mb-5 mt-5']")
        Acteurs_button.click()
        #choisir ligne
        ligne1 = driver.find_element(By.XPATH,"//tbody/tr[1]")
        #Mofication_Acteur
        Modifier_button = driver.find_element(By.XPATH,"//body[1]/app-root[1]/app-client[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[6]/div[1]/a[1]")
        Modifier_button.click()
        AjouN = driver.find_element(By.XPATH, "//input[@id='nom']")   
        AjouN.clear()
        AjouN.send_keys("ahmed2")
                #modifier Adresse
        AjouA = driver.find_element(By.XPATH, "//input[@id='adresse']")
        AjouA.clear()   
        AjouA.send_keys("Sfax2")
                #modifier numéro
        Ajout_Num = driver.find_element(By.XPATH, "//input[@id='numtelephone']")   
        Ajout_Num.clear()
        Ajout_Num.send_keys("58197236")  
                #modifier Type
        dropdown_element = driver.find_element(By.XPATH, "//select[@id='type']")
        dropdown = Select(dropdown_element)
        option_text = 'Entreprise'   
        dropdown.select_by_visible_text(option_text)
        #bouton Modifier
        Ajout_button = driver.find_element (By.XPATH,"//button[normalize-space()='Modifier']")
        Ajout_button.click()
        
        time.sleep(5)
    def tearDown(self):
        self.driver.close()
if __name__ == "__main__":
    unittest.main()