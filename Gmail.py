#!/usr/bin/python
# -*- coding: utf-8 -*-

import smtplib
import netrc
from secret import password, username #  Gmail password and username
from address import fromaddr, recipient #  added addresses here because I can

# Writing the message (You can write email in html format or plain text.)

msg = """
From: 
To: 
Subject:

Hello World
"""



#  Sending the mail

server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server_ssl.ehlo()  #  optional, called by login()
server_ssl.login(username, password)
server_ssl.sendmail(fromaddr, recipient, msg)
server_ssl.quit()
print('Sent email to %s' % recipient)



