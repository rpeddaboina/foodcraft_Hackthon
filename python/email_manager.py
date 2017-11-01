from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

class EmailManager():

	def __init__(self):
		self.mail=Mail(app)

		app.config['MAIL_SERVER']='smtp.gmail.com'
		app.config['MAIL_PORT'] = 465
		app.config['MAIL_USERNAME'] = 'hackathon.foodcraft@gmail.com'
		app.config['MAIL_PASSWORD'] = 'stage2@qa'
		app.config['MAIL_USE_TLS'] = False
		app.config['MAIL_USE_SSL'] = True
		self.mail = Mail(app)

	def send_email(self, subject, recepients, body):
		sender = app.config['MAIL_USERNAME']
		msg = Message(subject, sender, recepients)
		msg.body = body
		self.mail.send(msg)
		
