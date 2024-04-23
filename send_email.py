import smtplib, ssl
import os


def email_sender(message):
    host = "smtp.gmail.com"
    port = 465
    username = "senderpyemail@gmail.com"
    password = os.getenv("PASSWORD")
    recever = "popov.miroslav.85@gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, recever, message)