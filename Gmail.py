##!/usr/bin/python
# -*- coding: utf-8 -*-

### Last updated July 17 2016
### Martin O'Flaherty

import smtplib
from datetime import datetime
from seceret import username, password #  Gmail password and username more Secure 
from emailaddress import From, To, Subject, body #  added addresses here because I can


email_text = """\  
From: %s  
To: %s  
Subject: %s

%s
""" % (From, ", ".join(To), Subject, body)

#  Sending the mail over Gmail ssl server

server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server_ssl.ehlo()  #  optional, called by login()
server_ssl.login(username, password)
server_ssl.sendmail(From, To, Subject)
server_ssl.quit()
print "Your Email to %s was sent successfully" % (From,) # Format seemed a better option here rather than % string
print datetime.now().strftime("%d-%m-%y %H:%M:%S")
