import config as c
import smtplib


def send_email(msg):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(c.GMAIL_USERNAME, c.GMAIL_PASSWORD)

    msg_body = '\n\nThis email automatically pulls figures from the US treasury\n' \
               'and the New York Fed to calculate the probability of a recession\n' \
               'in a year\'s time.'

    msg += msg_body

    server.sendmail(c.GMAIL_USERNAME, c.GMAIL_USERNAME, msg)
    server.quit()
    print('Sent an email')
