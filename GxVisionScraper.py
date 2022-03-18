from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class AsociatedAgent:

    def __init__(self, url = "https://inter.com.ve/gxvision/"):
        
        self.url = url
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(self.url)
        self.username = ""
        self.password = ""

    def login(self, username, password):
        """
            Login into the system given the user and password of the AA
        """
        self.driver.find_element(By.ID,"vUSERLOGIN").send_keys(username)
        self.driver.find_element(By.CLASS_NAME,"Button_Standard").click()
        self.driver.find_element(By.ID,"vUSERPASSWORD").send_keys(password)

if __name__=='__main__':


    url = "https://inter.com.ve/gxvision/"
    username = "AASOINTEC"
    password = "Sointec34"
    
    Sointec = AsociatedAgent(url)
    Sointec.login(username, password)
    Sointec.driver.quit()

