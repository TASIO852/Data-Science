import time
from selenium import webdriver  # faz o passo manual dentro do whatsapp
from webdriver_manager.chrome import ChromeDriverManager  # acessa o whatsapp
from selenium.webdriver.common.keys import Keys  # aperta a tecla do teclado


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(40)
contatos = ["A"]  # trocar por mensagem nao lida
mensagem = 'Ola esta e uma mensagem automatica'


def enviar_mensagem(mensagem):
    campo_msg = driver.find_elements_by_xpath(
        '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    campo_msg[1].click()
    time.sleep(1)
    campo_msg[1].send_keys(mensagem)
    campo_msg[1].send_keys(Keys.ENTER)


def buscar_contato(contatos):
    campo_pesquisa = driver.find_elements_by_xpath(
        '//*[@id="side"]/div[1]/div/label/div/div[2]')
    time.sleep(1)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contatos)
    campo_pesquisa.send_keys(Keys.ENTER)


for contato in contatos:
    buscar_contato(contatos)
    enviar_mensagem(mensagem)
