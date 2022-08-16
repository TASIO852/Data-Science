import os  # quebra de linha
import sys  # finalizar conversasao
import time
import openpyxl  # criaçao de planilhas
# configuraçaoes do webdriver/chorme
from selenium.webdriver.chrome.options import Options
import pywhatkit  # acessa o whatsapp e faz o envio da msg
import keyboard  # aperta a tecla do teclado
from datetime import datetime
from selenium.webdriver.common.by import By


# inicializaçao do programa
def __init__(self):
    envio_das_msg()

# mensagens nao lidas do usuario


def msg_n_lida():
    # identificar msg que chegaram
    msg_chegou = By.find_element_by_xpath(
        '//*[@id="pane-side"]/div[1]/div/div/div[9]/div/div/div[2]/div[2]/div[2]/span[1]/div[2]/span')
    time.sleep(1)
    if msg_chegou:
        leia_msg = By.find_element_by_xpath(
            '//*[@id="pane-side"]/div[1]/div/div/div[10]/div/div/div[2]/div[2]/div[1]/span/span')
        leia_msg.click()  # trocar por keyboards
        time.sleep(1)

# perguntas para o usuario


def perguntas_usuario(nome):
    # pedir o nome
    nome = input('Digite seu nome: ')  # jogar para escopo global
    # pedir o CPF
    cpf = input('Digite seu CPF: ')  # jogar para escopo global
    # Apresentar o chatbot
    print(
        f'Ola tudo bem {nome} esta na auto escola BH.{os.linesep}ESTA E UMA MENSAGEM AUTOMATICA ESCOLHA UMA DAS OPÇÕES ABAIXO:')
    while True:
        # Oferer o menu de opções
        resposta = input(
            f'O que gostaria de saber hoje?{os.linesep}[1] - Vale a pena aprender Python?{os.linesep}[2] - Quanto tempo leva para conseguir um emprego com Python?{os.linesep}[3] - Quando vou saber que estou BOM o suficiente para conseguir um emprego?{os.linesep}[4] - Onde me recomenda estudar Python para conseguir um emprego hoje?{os.linesep}[5] - Finalizar perguntas{os.linesep}'
        )
    # enviar a resposta
        resposta_usuario(resposta, nome)

# respostas para o usuario


def resposta_usuario(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome} na minha visão vale muito apena, isso porque Python é uma das linguagens que mais cresce no mundo e possui salários mensais que vão desde R$2100,00 a até mais R$10000,00 no Brasil, além de contar com uma média anual de $85.000 dolares nos EUA.{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome} isso varia muito com o nível de esforço, dedicação e busca diária por vagas de cada indivíduo. Alguns conseguem com menos de 3 meses e outros com mais, tudo depende do quanto você já sabe ou está disposto a correr atrás para aprender.{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome}, primeiro entenda, ninguém vai te dizer ou chegar magicamente um dia e te dizer que você está BOM o suficiente para conseguir um emprego ou fazer dinheiro com seu conhecimento de programação, seja em Python ou qualquer outra linguagem ou habilidade, você simplesmente tem que começar dar a sua cara a tapa e começar a aplicar para oportunidades ou até mesmo começar a criar elas, desde o dia que você já domina os fundamentos de uma linguagem(se estamos falando de Python, recomendo aprender no mínimo os 5 pilares de programação.{os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep}{nome} você pode estudar através de vídeos gratúitos no YouTube, livros e sites de programação, porém se buscar um lugar com suporte 1 a 1, estrutura sequencial, projetos novos todos os meses dos ano e um curso que vai te ensinar toda a base e habilidades mais lucrativas que precisa para criar aplicações em python e estar pronto para o mercado, recomendo o cursodepython.net.{os.linesep}')
    elif resposta == '5':
        # comando para sair das perguntas
        print(f'Obrigado por responder {nome} e boa sorte !!')
        # talvez tire o ctrl + w pq ele apaga a aba do wpp
        keyboard.press_and_release('ctrl + w')
        sys.exit()  # eu fecho o programa para todo mundo eo bot para de funcionar ???
    else:
        print('Digite apenas 1, 2, 3, 4 ou 5 para sair')

# envio da mensagem


def envio_das_msg():
    while len(msg_n_lida) >= 1:
        # enviando msg para contatos da lista começando do contato [0]
        pywhatkit.sendwhatmsg(msg_n_lida[0],
                              perguntas_usuario,
                              datetime.now().hour, datetime.now().minute + 2)
        # nao enviar a mesma msg para o mesmo contato (talvez eu tire pq presiso incluir o numero na planilha)
        del msg_n_lida[0]  # talvez eu tire vai atrapalhar processo
        time.sleep(30)
