import config as c

import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

server.login(c.GMAIL_USERNAME, c.GMAIL_PASSWORD)

msg = 'fuck you'
server.sendmail(c.GMAIL_USERNAME, 'stanley.kaymen@gmail.com', msg)