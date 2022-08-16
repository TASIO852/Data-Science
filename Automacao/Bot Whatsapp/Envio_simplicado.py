import pywhatkit #acessa o whatsapp
import keyboard #aperta a tecla do teclado
import time
from datetime import datetime
from chatbot_coversa_options import enviar_msg
contatos = ['+5527997477241']
msg = 'Msg automatica S2'
while len(contatos) >= 1:
    # enviar mensagem
    pywhatkit.sendwhatmsg(contatos[0], enviar_msg, datetime.now().hour, datetime.now().
    minute + 2)
    del contatos[0]
    time.sleep(40)
keyboard.press_and_release('ctrl + w')  