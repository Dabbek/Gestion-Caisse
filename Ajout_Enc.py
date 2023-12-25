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
        # #Ajout_Image
        Ajout_Enc_button = driver.find_element(By.XPATH," //span[@class='text d-none d-sm-inline']")
        Ajout_Enc_button.click()
        image_path =r"C:\Users\TPC\Desktop\Test automatique\image.png"
        input_file_1 = driver.find_element(By.ID, "fileInput")
        input_file_1.send_keys(image_path)
        Ajouter= driver.find_element(By.XPATH,"//button[normalize-space()='Ajouter']")
        Ajouter.click()      
    time.sleep(10)
    # def tearDown(self):
    #     self.driver.close()
    
if __name__ == "__main__":
    unittest.main()