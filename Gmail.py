#!/usr/bin/python
# -*- coding: utf-8 -*-

import email
import re
import smtplib
import netrc
from secret import password, username #  Gmail password and username
from address import fromaddr, recipient #  added addresses here because I can
from RawMail import msg, html #  added addresses here because I can
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#  Record the MIME types of both parts - text/plain and text/html.

part1 = MIMEText(msg, 'plain')
part2 = MIMEText(html, 'html')

#  Sending the mail over Gmail ssl server

server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server_ssl.ehlo()  #  optional, called by login()
server_ssl.login(username, password)
server_ssl.sendmail(fromaddr, recipient, msg)
server_ssl.quit()
print "Your Email to %s was sent successfully" % (recipient,) #  .format seemed a better option here rather than % string



