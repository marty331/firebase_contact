#!/usr/bin/env python

from firebase import Firebase
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import json
import logging

firebase = Firebase('https://YOURFIREBASE.firebaseio.com/contacts')

contact_list = firebase.get()
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
fromaddr = ‘YOUR_ALT_GMAIL@gmail.com'
toaddr = ‘YOUR_REAL@EMAIL.COM’
msg = MIMEMultipart()
msg['From'] = formatter
msg['To'] = toaddr

server.login(fromaddr, ‘YOUR_PASSWORD’)
for cl in contact_list:
	contact_name = str(contact_list[cl]['name'])
	contact_phone = str(contact_list[cl]['phone'])
	contact_email = str(contact_list[cl]['email'])
	contact_message = str(contact_list[cl]['message'])
	contact_type = str(contact_list[cl]['type'])
	contact_pref = str(contact_list[cl]['contact'])
	try:
		contact_view = str(contact_list[cl]['viewed'])
	except Exception, e:
		contact_view = 'Y'
		logging.info(e)
	if contact_view == 'N':
		body = 'You have a new contact:<b> ' + contact_name + '</b> who would like to be contacted via ' + contact_pref	+ ' email address is: ' + contact_email + ' and phone is: ' + contact_phone + '. <br><br>The contact type is '+ contact_type + ' and the message is <br>' + contact_message
		msg['Subject'] = 'New Contact: '+contact_name
		msg.attach(MIMEText(body, 'HTML'))
		text = msg.as_string()
		server.sendmail(fromaddr, toaddr, text)
		contact_list[cl]['viewed']='Y'
		firebase.update(contact_list)

server.quit()

