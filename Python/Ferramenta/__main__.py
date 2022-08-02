import PySimpleGUI as sg
import os

# Script modularizado
import pdf_extrator as pdf
import Conversor_pdf as cpdf
import Converso_xml as xml
import Email as em
import Merge_xlsx as xls

working_directory = os.getcwd()

# Designer da interface 
def escolha():
    layout1 = [
        
    [sg.Combo(['New York','San Fransisco'],default_value='Utah',key='board')],
    [sg.Button('Continuar'), sg.Exit()]
]
    return sg.Window("Escolha",layout=layout1)

def ferramentas():
    layout = [
        
        # Excel Files 
        [sg.Text("Coloque seu Excel aqui:")],
        [sg.InputText(key="-FILE_PATH1-"),sg.FileBrowse(initial_folder=working_directory, file_types=[("CSV Files", "*.csv")])],
        [sg.InputText(key="-FILE_PATH2-"),sg.FileBrowse(initial_folder=working_directory, file_types=[("CSV Files", "*.csv")])],
        [sg.Button('Unificar'), sg.Exit()],
        
        # pdf Files
        [sg.Text("Coloque seu PDF aqui:")],
        [sg.InputText(key="-FILE_PATH3-"),sg.FileBrowse(initial_folder=working_directory, file_types=[("PDF", "*.pdf")])],
        [sg.Button('Gerar Excel'), sg.Exit()],
        
        # pdf Files
        [sg.Text("Coloque seu PDF aqui:")],
        [sg.InputText(key="-FILE_PATH4-"),sg.FileBrowse(initial_folder=working_directory, file_types=[("PDF", "*.pdf")])],
        [sg.Button('Extract pdf'), sg.Exit()],
        
        # Email addresses
        [sg.Text("Enter full name:"), sg.Input(key='-NAME-', do_not_clear=True, size=(20, 1))],
        [sg.Text("Enter your email address:"), sg.Input(key='-EMAIL_ADDRESS-', do_not_clear=True, size=(10, 1))],
        [sg.InputText(key="-FILE_PATH5-"),sg.FileBrowse(initial_folder=working_directory, file_types=[("Excel", "Files", "*.xlsx")])],
        [sg.Button('Send Email'), sg.Exit()],
        
        # Conversor XMl
        [sg.InputText(key="-FILE_PATH6-"),sg.FileBrowse(initial_folder=working_directory, file_types=[("XML Files", "*.xml")])],
        [sg.Button('Converter'), sg.Exit()],
        
        [sg.Button('Voltar'), sg.Exit()]
    ]

    return sg.Window("Ferramentas",layout=layout)

# Varias janelas na aplicaçao
janela1,janela2 = escolha(),None
while True:
    window,event,values = sg.read_all_windows()
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    if window == janela1 and event == 'Continuar':
        janela2 = ferramentas()
        janela1.hide()
    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()

# logica de funcionamento da interface 
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    
# Excel path
    elif event == "Submit":
        csv_address1 = values["-FILE_PATH1-"]
        csv_address2 = values["-FILE_PATH2-"]
        xls.merge_excel(csv_address1, csv_address2)  
        
# Conversor pdfload
    elif event == "Gerar Excel":
        conversao = values["-FILE_PATH3-"]
        cpdf.convert_pdf(conversao)
        
# Extract pdfload
    elif event == "Extract pdf":
        extracao = values["-FILE_PATH4-"]
        pdf.extrator_pdf(extracao)
        
# xml file path
    elif event == "Converter":
        xml_file = values["-FILE_PATH5-"]
        xml.conversor_xml(xml_file)
            
# Email address path 
    elif event == 'Send Email':
        validation_result = em.validate(values)
        if validation_result[0]:
            em.send_email(values['-MESSAGE-'], values['-EMAIL_ADDRESS-'])
            sg.popup('EMAIL SENT!')
        else:
            error_message = em.generate_error_message(validation_result[1])
            sg.popup(error_message)            

# Transformando em um executavel usando pyinstaller

# pyinstaller ferramenta.py
# pyinstaller --onefile --noconsole./nome do arquivo.py
