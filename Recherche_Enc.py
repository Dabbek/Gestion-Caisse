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
        #acces Section Encaissement 
        Acteurs_button = driver.find_element(By.XPATH," //a[@href='encaissement']//div[@class='d-flex align-items-center']")
        Acteurs_button.click()
        #icone de recherche
        Modifier_button = driver.find_element(By.XPATH,"//div[@class='btn btn-primary mt-5 mr-2 btn-icon-split position-custom float-right d-none d-md-inline']")
        Modifier_button.click()
        #par id 
        Par_ID = driver.find_element(By.XPATH, "//input[@placeholder='Par ID']")   
        Par_ID.clear()
        Par_ID.send_keys("2")
        #par Client 
        Par_Client = driver.find_element(By.XPATH, "//div[@id='wrapper']//div[@class='form-row']//div[2]//select[1]")
        Par_Client.send_keys("Ahmed2")
        #Par Ticket
        Par_Ticket = driver.find_element(By.XPATH, "//input[@placeholder='Par ticket']")   
        Par_Ticket.send_keys("58197236") 
        #Par Montant 
        Par_Montant = driver.find_element(By.XPATH, "//input[@placeholder='Par Montant'] ")   
        Par_Montant.send_keys("111") 
        #Par Description  
        Par_Description  = driver.find_element(By.XPATH, "//input[@placeholder='Par description'] ")   
        Par_Description .send_keys("Ajoutet Ticket ") 
        # Par_Date
        date_input = driver.find_element(By.XPATH,"//div[@class='form-group col-md-3']//input[@type='date']")
        date_input.clear()
        date_input.send_keys("07/07/2023")  
        
        Acteurs_button = driver.find_element(By.XPATH,"//button[@class='form-control btn btn-outline-secondary']")
        Acteurs_button.click()
          
    time.sleep(10)
    # def tearDown(self):
    #     self.driver.close()
if __name__ == "__main__":
    unittest.main()