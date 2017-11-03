#! /home/ubuntu/.virtualenvs/FoodCraft/bin/python
from flask import Flask, request, Response
import requests
import json
from email_manager import EmailManager
from db_manager import DBManager

app = Flask(__name__)

@app.route("/send-email", methods=['GET', 'POST'])
def send_email():
	em = EmailManager()
	su = "Test mail from Hackathon"
	bd = "Hi, this is a test mail. Sent latest."
	print("Sending email...")
	em.send_email(su, 'sridhar.ka79@yahoo.com', bd)
    	print("done.")
	response = app.response_class(
                response=json.dumps('Success'),
                status=200,
                mimetype='application/json'
        )
        return response


def send_email_with_link(p_fname, p_lname, p_email, course_id, course_name, course_img_file):
	course_url = "https://meet.jit.si/cs%s" %course_id 
	em = EmailManager()
	text1 = "<p>Dear %s %s,</p><p></p><p>You hav been successfully enrolled into the Course: %s</p>" %(p_fname, p_lname, course_name)
	text = "<p></p><p>Please use the below details to join this session as per the Schedule:</p>"
	#text += "<p>&emsp;&emsp;Schedule:</p><p></p><p>&emsp;&emsp;&emsp;Date: 11/10/2017</p><p>&emsp;&emsp;&emsp;Start Time: 2:00 PM PST</p>"
	text += "<p></p><p>&emsp;&emsp;&emsp;Date: 11/10/2017</p><p>&emsp;&emsp;&emsp;Start Time: 2:00 PM PST</p>"
	text += "<p>&emsp;&emsp;&emsp;End Time:  3:00 PM PST</p><p>&emsp;&emsp;&emsp;Meeting url: %s</p>" %course_url
	text += "<p></p><p></p>See you in the classroom.<p></p><p></p>"
	text += "<p>Thanks,</p><p>Food Craft Team</p>"
	subj = "Enrollment to the course: %s" %course_name
	rcpnt = p_email
	em.send_email(subj, rcpnt, text1, text, course_img_file) 		
	

@app.route("/enroll", methods=['POST'])
def enroll_student():
	print("request.data = ", request.data )
	data = request.json
	print("data = ", data)
	course_id = data['courseid']
	p_email = data['email']	
	p_fname = data['firstname']
	p_lname = data['lastname']
	
	dbm = DBManager()
	qry = 'select Name, Image_File from Courses where Id = %s and Status = "1"' %course_id
	course_details = dbm.execute_query(qry)
	course_name = course_details[0][0]
	course_img_file = course_details[0][1]
	send_email_with_link(p_fname, p_lname, p_email, course_id, course_name, course_img_file)

	response = app.response_class(
		response=json.dumps('Success'),
		status=200,
		mimetype='application/json'
	)
	return response


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=9099) #debug = True)
