import config as c
import smtplib

def send_email(msg):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(c.GMAIL_USERNAME, c.GMAIL_PASSWORD)
    server.sendmail(c.GMAIL_USERNAME,c.GMAIL_USERNAME, msg)
    print('Sent an email')
