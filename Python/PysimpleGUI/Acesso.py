from selenium import webdriver
import time

class Heineken:

    def __init__(self):
        self.site_link = "http://parceiros.heineken.com.br/irj/portal"
        self.site_map = {
            "user":{
                "nome":{
                    "xpath": '//*[@id="logonuidfield"]'
                }
            }

        }
        
        self.driver = webdriver.Chrome(
            executable_path="C:/Users/tasio.guimaraes/Documents/Data-Science/Python/Codes/Driver/chromedriver.exe")
        self.driver.maximize_window()

    def abrir_site(self):
        time.sleep(2)
        self.driver.get(self.site_link)
        time.sleep(10)

    def usuario(self):
        self.driver.find_element_by_xpath(self.site_map["user"]["nome"]["xpath"]).click()
        
    

teste = Heineken()
teste.abrir_site()