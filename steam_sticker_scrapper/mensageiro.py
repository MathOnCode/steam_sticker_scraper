import os
from os import getenv
import smtplib
from email.message import EmailMessage

def enviar_email_com_anexo(destinatario, assunto, corpo, arquivo_caminho):
    EMAIL_REMETENTE = getenv("EMAIL_USER")
    SENHA_REMETENTE = getenv("EMAIL_PASSWORD")

    msg = EmailMessage()
    msg['Subject'] = assunto
    msg['From'] = EMAIL_REMETENTE
    msg['To'] = destinatario
    msg.set_content(corpo)

    with open(arquivo_caminho, 'rb') as f:
        dados_pdf = f.read()
    msg.add_attachment(dados_pdf, maintype='application', subtype='pdf', filename=os.path.basename(arquivo_caminho))

    with smtplib.SMTP(getenv("EMAIL_HOST"), int(getenv("EMAIL_PORT"))) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(EMAIL_REMETENTE, SENHA_REMETENTE)
        smtp.send_message(msg)

    print("Email enviado para", destinatario)