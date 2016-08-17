##!/usr/bin/python
# -*- coding: utf-8 -*-

# Last updated July 17 2016
# Martin O'Flaherty

import smtplib
from datetime import datetime

# Gmail password and username more Secure
from seceret import username, password

# added addresses here because I can
from emailaddress import From, To, Subject, body


email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (From, ", ".join(To), Subject, body)

#  Sending the mail over Gmail ssl server

server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server_ssl.ehlo()
server_ssl.login(username, password)
server_ssl.sendmail(From, To, Subject)
server_ssl.quit()
print "Your Email to %s was sent successfully" % (From,)
print datetime.now().strftime("%d-%m-%y %H:%M:%S")
