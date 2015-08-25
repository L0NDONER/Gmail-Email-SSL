#!/usr/bin/python2

import smtplib
import hashlib
 
# Replace **** with your to and from addresses

fromaddr = '****@gmail.com'
toaddrs = '****@gmail.com'

# Message of the email enclosed in three """
# Speach marks so you can add plain text or HTML,
# finishing with three Speach marks """
# replace Yourname and 
# Personsname with your own and recipiants
#Replace **** with your gmail address
#replace anyemailaddress with recipiants email address

msg = """From: YourName <******@****>
To: PersonsName <******@anyemailaddress>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP HTML e-mail test.

Hello World

This is my first Mako Test
"""

# Login Gmail Details

username = '*****'  # Replce with your G username
password = '****'  # Replace ******* with your Google Password

# Hashlib Sha Cryptographic hashes and message digests.

h = hashlib.sha224()
h.update(msg)
print h.hexdigest()  # Will print the Cryptographic key

passwd = "mypass"
passwd = bytes(passwd)
passwd = hashlib.sha224("****").hexdigest()  # *** replace with password

# SMTP_SSL SSL connection to Google

server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server_ssl.ehlo()  # optional, called by login()
server_ssl.login(username, password)
server_ssl.sendmail(fromaddr, toaddrs, msg)
server_ssl.quit()
print 'successfully sent the Email'

