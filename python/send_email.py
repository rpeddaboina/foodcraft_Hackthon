#! /home/ubuntu/.virtualenvs/FoodCraft/bin/python
from flask import Flask
from email_manager import EmailManager

app = Flask(__name__)

@app.route("/")
def index():
	em = EmailManager()
	su = "Test mail from Hackathon"
	bd = "Hi, this is a test mail."
	em.send_email(su, ['rpeddaboina@paypal.com', 'sridhar.ka79@yahoo.com'], bd)
	return "sent"

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=9099) #debug = True)
