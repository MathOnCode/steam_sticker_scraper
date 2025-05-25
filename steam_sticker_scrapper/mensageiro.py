import os
from os import getenv
import smtplib
from email.message import EmailMessage

def enviar_email_com_anexos(destinatario, assunto, corpo, lista_de_arquivos):
    EMAIL_REMETENTE = getenv("EMAIL_USER")
    SENHA_REMETENTE = getenv("EMAIL_PASSWORD")
    EMAIL_HOST = getenv("EMAIL_HOST")
    EMAIL_PORT = int(getenv("EMAIL_PORT"))

    msg = EmailMessage()
    msg['Subject'] = assunto
    msg['From'] = EMAIL_REMETENTE
    msg['To'] = destinatario
    msg.set_content(corpo)

    for arquivo_caminho in lista_de_arquivos:
        try:
            with open(arquivo_caminho, 'rb') as f:
                dados = f.read()
                nome_arquivo = os.path.basename(arquivo_caminho)
                msg.add_attachment(dados, maintype='application', subtype='pdf', filename=nome_arquivo)
        except FileNotFoundError:
            print(f"Arquivo não encontrado: {arquivo_caminho}")
        except Exception as e:
            print(f"Erro ao anexar o arquivo '{arquivo_caminho}': {e}")

    with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(EMAIL_REMETENTE, SENHA_REMETENTE)
        smtp.send_message(msg)

    print("Email enviado para", destinatario)
