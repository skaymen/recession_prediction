import config as c

import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)

server.login()