import pandas as pd 
import win32com.client as win32

def matinal(excel):
    # # importar a base de dados
    # tabela_vendas = pd.read_excel(excel)

    # # visualizar a base de dados
    # pd.set_option('display.max_columns', None)
    # print(tabela_vendas)

    # # faturamento por loja
    # faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby(
    #     'ID Loja').sum()
    # print(faturamento)

    # # quantidade de produtos vendidos por loja
    # quantidade = tabela_vendas[['ID Loja', 'Quantidade']].groupby(
    #     'ID Loja').sum()
    # print(quantidade)

    # print('-' * 50)
    # # ticket médio por produto em cada loja
    # ticket_medio = (faturamento['Valor Final'] /
    #                 quantidade['Quantidade']).to_frame()
    # ticket_medio = ticket_medio.rename(columns={0: 'Ticket Médio'})
    # print(ticket_medio)

    # enviar um email com o relatório
    outlook = win32.Dispatch('outlook.application')
    
    # eduardo.rodrigues@syno.com.br
    mail = outlook.CreateItem(0)
    mail.To = 'cristiane.santos@syno.com.br'
    mail.Subject = 'Relatório de Vendas por Loja'
    mail.HTMLBody = f'''
    <p>Prezados,</p>

    <p>Segue o Relatório de Vendas por cada Loja.</p>

    <p>Faturamento:</p>
    {faturamento.to_html(formatters={'Valor Final': 'R${:,.2f}'.format})}

    <p>Quantidade Vendida:</p>
    {quantidade.to_html()}

    <p>Ticket Médio dos Produtos em cada Loja:</p>
    {ticket_medio.to_html(formatters={'Ticket Médio': 'R${:,.2f}'.format})}

    <p>Qualquer dúvida estou à disposição.</p>

    <p>Att.,</p>
    <p>Lira</p>
    '''

    mail.Send()

    print('Email Enviado')

# Email config de server dns
import smtplib, ssl

def send_email(message, recipient_email):
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email="studyiochannel@gmail.com"
    password = "studyio23"

    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, recipient_email, message)
    except Exception as e:
        print(e)
    finally:
        server.quit()

import PySimpleGUI as sg
# import email_interface

sg.theme('Black')

layout = [
]

window = sg.Window('Python Email Client', layout)

def validate(values):
    is_valid = True
    values_invalid = []

    if len(values['-NAME-']) == 0:
        values_invalid.append('Name')
        is_valid = False
    
    if len(values['-EMAIL_ADDRESS-']) == 0:
        values_invalid.append('Passport Number')
        is_valid = False
    
    if '@' not in values['-EMAIL_ADDRESS-']:
        values_invalid.append('Email Address')
        is_valid = False
    
    if len(values['-MESSAGE-']) == 0:
        values_invalid.append('MESSAGE')
        is_valid = False

    result = [is_valid, values_invalid]
    return result

def generate_error_message(values_invalid):
    error_message = ''
    for value_invalid in values_invalid:
        error_message += ('\nInvalid' + ':' + value_invalid)

    return error_message

while True:
    event, values = window.read()

window.close()
