from flask import Flask
from flask_mail import Mail, Message
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
import os

app = Flask(__name__)

class EmailManager():

	def __init__(self):
		#self.mail=Mail(app)

		app.config['MAIL_SERVER']='smtp.gmail.com'
		app.config['MAIL_PORT'] = 587 #465
		app.config['MAIL_USERNAME'] = 'hackathon.foodcraft@gmail.com'
		app.config['MAIL_PASSWORD'] = 'stage2@qa'
		app.config['MAIL_USE_TLS'] = False
		app.config['MAIL_USE_SSL'] = True
		#self.mail = Mail(app)

	def send_email(self, subject, recepients, hl, body, course_img_file):
		s = smtplib.SMTP(host=app.config['MAIL_SERVER'], port=app.config['MAIL_PORT'])
		msg = MIMEMultipart()
		msg['Subject'] = subject #'Enrollement into course'
		msg['From'] = app.config['MAIL_USERNAME'] #'FoodCraft100'
		msg['To'] = recepients[0]
		s.ehlo()
		s.starttls()
		s.ehlo()
		s.login(app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])

		# Record the MIME types of both parts - text/plain and text/html.
		part1 = MIMEText(hl, 'plain')
		part2 = MIMEText(body, 'plain')

		# Attach parts into message container.
		# According to RFC 2046, the last part of a multipart message, in this case
		# the HTML message, is best and preferred.
		msg.attach(part1)
		course_img_file = "images/" + course_img_file
		img_data = open(course_img_file, "rb").read()
		img = MIMEImage(img_data, name=os.path.basename(course_img_file))
		msg.attach(img)
		msg.attach(part2)

		s.sendmail('FoodCraft', msg['To'], msg.as_string()) 
		s.quit()
