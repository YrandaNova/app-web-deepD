import os
import ssl
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv
import schedule
import time
import csv
import os 




load_dotenv()
#funcion que envia mails con pdf o csv
def send_email(email_recipient, pdf_path):
    email_sender = 'mfcr11022000@gmail.com'
    password = os.getenv("EMAIL_PASSWORD")

    smtp_port = 587
    smtp_server = "smtp.gmail.com"
    message = MIMEMultipart()
    message["From"] = email_sender
    message["To"] = email_recipient
    message["Subject"] = "Hello, world!"

    # Attach the PDF file
    with open(pdf_path, "rb") as pdf_file:
        attachment = MIMEBase("application", "pdf")
        attachment.set_payload(pdf_file.read())
        encoders.encode_base64(attachment)
        attachment.add_header(
            "Content-Disposition",
            f"attachment; filename={os.path.basename(pdf_path)}"
        )
        message.attach(attachment)

    email_context = ssl.create_default_context()

    try:
        print("Connecting to the server...")
        TIE_server = smtplib.SMTP(smtp_server, smtp_port)
        TIE_server.starttls(context=email_context)
        TIE_server.login(email_sender, password)
        print("Connected.")

        print(f"Sending email to: {email_recipient}")
        TIE_server.send_message(message)
        print(f"Email successfully sent to: {email_recipient}")

    except Exception as e:
        print(e)

    finally:
        TIE_server.quit()


#funcion que borra el contenido del csv

def clear_csv(file_path):
    with open(file_path, "w", newline="") as csvfile:
        csvfile.truncate()

#funcion que manda csv y borra contenido

def send_Admin():
    email_res='mayrafercamacho@gmail.com'
    path=os.path.abspath('prueba/resumen.csv')
    send_email(email_res,path)
    #send_email('michele@dive.ai',path)
    clear_csv(path)


# manda un correo dependiendo de un tiempo determinado

#schedule.every().day.at("22:45").do(send_Admin)

# Keep the program running indefinitely






# Usage example


"""
clear_csv('prueba/resumen.csv')
email_recipient = 'mayrafercamacho@gmail.com'
pdf_path = "/home/yranda/Documents/Deep_dive/prueba/Watermarked.pdf"
csv='/home/yranda/Documents/Deep_dive/prueba/titulo.csv'
send_email(email_recipient, csv)
"""