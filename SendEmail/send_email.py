#!/usr/bin/python

import smtplib

def send_mail():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	server.login('shakilk1729@gmail.com','wrewre53455wewruqqn')
	subject = 'Price fell down'
	body = "Check the data link"

	msg = f"Subject: {subject}\n\n{body}"

	print("Now sending the actual email..data test email")
	server.sendmail(
		'shakilk1729@gmail.com',
		'example@exampletest.com',
		msg
	)

	server.quit()
	print("email has been send as the price rose")

send_mail()
