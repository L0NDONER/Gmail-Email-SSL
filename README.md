######################################################
#                                                    #
#    Python Gmail SSL Script Version 2               #
#    Sha Cryptographic hashes message.               #
#    Author: L0NDONER                                #
#                                                    #
######################################################

Gmail.py

A common task for system administrators and developers is to use scripts to send
emails if an error occurs.

Using Googles SMTP servers are free to use and works perfectly fine to relay
emails. 

Note that Google has a sending limit: "Google will temporarily disable your
account if you send messages to more than 500 recipients or if you send a large
number of undeliverable messages. "

As long as you are fine with that, you are good to go.

Sending mail is done with Python's smtplib using an SMTP (Simple Mail Transfer
Protocol) server.

Since we will use Google's SMTP server to deliver our emails, we will need to
gather information such as server, port, authentication. 

That information is easy to find with a Google search.

=========================================================

Outgoing Mail (SMTP) Server - requires TLS or SSL:
smtp.gmail.com

Use Authentication:
Yes

Port for TLS/STARTTLS:
587

Port for SSL:  ####### the script uses SSL so uses this port Number  #######
465

Server timeouts:
Greater than 1 minute, we recommend 5

Account Name or User Name:
your full email address (including @gmail.com or @your_domain.com)

Email Address: 
your email address (username@gmail.com or username@your_domain.com)

Password:
your Gmail password

=========================================================

This is a Python script for Gmail.
Send securely over SSL Hashlib, Sha Cryptographic hashes the message digests.
the script will print the Crypto key and print the Email has been successfully sent.

=========================================================

DEPENDENCIES:

import smtplib
import hashlib


========================================================

You are free to use and modify to your own needs if you wish.


LICENSE:

GNU General Public License, version 2 (GPL-2.0)
