from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from enum import IntEnum

class MainMenu(IntEnum):
    Default = 0
    Conf_Operativa = 1
    Atencion_al_cliente = 2
    Comercial = 3
    Div_Geografica = 4
    Tecnica = 5

class SecondMenu(IntEnum):
    Conf_Tecnica = 0
    CRM = 1
    Contratos = 2
    Base_de_Datos_Geografica = 3
    HeadEnd = 4
    Almacen = 5

class Options(IntEnum):
    Cambiar_Permisor = 0
    Marcas_de_Cable_Modem = 1
    Bandeja_Entrada_de_Email = 2
    Contactos = 3
    Venta_HFC_Agente_Autorizado = 4
    Contrato_Cable = 5
    Casa = 6
    Estado_ONU = 7
    Cola_815 = 8
    Cable_Modem = 9

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
        self.driver.find_element(By.ID,"vUSERPASSWORD").send_keys(password)
        self.driver.find_element(By.CLASS_NAME,"Button_Standard").click()

    def logout(self):
        self.driver.find_element(By.CLASS_NAME,"Button_HeaderClose").click()

    def get_menu(self):
        self.mainMenu = self.driver.find_elements(By.CLASS_NAME,"ThemeBlackMainFolderText")
        self.secondMenu = self.driver.find_elements(By.CLASS_NAME,"ThemeBlackMenuFolderRight")
        self.optionMenu = self.driver.find_elements(By.CLASS_NAME,"ThemeBlackMenuItemText")

    def goto_Cambiar_Permisor(self):
        self.get_menu()
        self.mainMenu[MainMenu.Default].click()
        self.optionMenu[Options.Cambiar_Permisor].click()

    def goto_Marcas_de_Cable_Modem(self):
        self.get_menu()
        self.mainMenu[MainMenu.Conf_Operativa].click()
        self.secondMenu[SecondMenu.Conf_Tecnica].click()
        self.optionMenu[Options.Marcas_de_Cable_Modem].click()

    def goto_Bandeja_Entrada_de_Email(self):
        self.get_menu()
        self.mainMenu[MainMenu.Atencion_al_cliente].click()
        self.secondMenu[SecondMenu.CRM].click()
        self.optionMenu[Options.Bandeja_Entrada_de_Email].click()

    def goto_Contactos(self):
        try:
            self.get_menu()
            self.mainMenu[MainMenu.Atencion_al_cliente].click()
            self.secondMenu[SecondMenu.CRM].click()
            self.optionMenu[Options.Contactos].click()
        except:
            print("option not available")
        else:
            if(not self.is_authorized()):
                self.driver.back()

    def goto_Venta_HFC_Agente_Autorizado(self):
        self.get_menu()
        self.mainMenu[MainMenu.Atencion_al_cliente].click()
        self.secondMenu[SecondMenu.CRM].click()
        self.optionMenu[Options.Venta_HFC_Agente_Autorizado].click()

    def goto_Contrato_Cable(self):
        self.get_menu()
        self.mainMenu[MainMenu.Comercial].click()
        self.secondMenu[SecondMenu.Contratos].click()
        self.optionMenu[Options.Contrato_Cable].click()

    def goto_Casa(self):
        self.get_menu()
        self.mainMenu[MainMenu.Div_Geografica].click()
        self.secondMenu[SecondMenu.Base_de_Datos_Geografica].click()
        self.optionMenu[Options.Casa].click()

    def goto_Estado_ONU(self):
        self.get_menu()
        self.mainMenu[MainMenu.Tecnica].click()
        self.secondMenu[SecondMenu.HeadEnd].click()
        self.optionMenu[Options.Estado_ONU].click()

    def goto_Cola_815(self):
        self.get_menu()
        self.mainMenu[MainMenu.Tecnica].click()
        self.secondMenu[SecondMenu.HeadEnd].click()
        self.optionMenu[Options.Cola_815].click()

    def goto_Cable_Modem(self):
        self.get_menu()
        self.mainMenu[MainMenu.Tecnica].click()
        self.secondMenu[SecondMenu.Almacen].click()
        self.optionMenu[Options.Cable_Modem].click()

    def test_menu(self):

        input("goto_Cambiar_Permisor")
        self.goto_Cambiar_Permisor() # No autorizado

        input("Go to Marcas de Cable Modem")
        self.goto_Marcas_de_Cable_Modem()

        input("goto_Bandeja_Entrada_de_Email")
        self.goto_Bandeja_Entrada_de_Email()

        input("goto_Contactos")  # No autorizado
        self.goto_Contactos()

        input("goto_Venta_HFC_Agente_Autorizado")
        self.goto_Venta_HFC_Agente_Autorizado()

        input("goto_Contrato_Cable")
        self.goto_Contrato_Cable() # No autorizado
        input("goto_Casa")

        self.goto_Casa()
        input("goto_Estado_ONU")
        self.goto_Estado_ONU()

        input("goto_Cola_815")
        self.goto_Cola_815()

        input("goto_Cable_Modem")
        self.goto_Cable_Modem()

        input("END Menu")

    def is_authorized(self):
        if "Not authorized" in self.driver.title:
            return False
        else:
            return True

def login():
    url = "https://inter.com.ve/gxvision/"
    username = "AASOINTEC"
    password = "Sointec34"
    
    Sointec = AsociatedAgent(url)
    Sointec.login(username, password) 
    return Sointec

if __name__=='__main__':


    url = "https://inter.com.ve/gxvision/"
    username = "AASOINTEC"
    password = "Sointec34"
    
    Sointec = AsociatedAgent(url)
    Sointec.login(username, password)    

    Sointec.test_menu()
    Sointec.logout()
    Sointec.driver.quit()
    #<title>K2B Not Authorized</title>

