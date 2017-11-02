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
	print "Sending email..."
	em.send_email(su, 'sridhar.ka79@yahoo.com', bd)
    	print "done."
	response = app.response_class(
                response=json.dumps('Success'),
                status=200,
                mimetype='application/json'
        )
        return response


def send_email_with_link(p_fname, p_lname, p_email, course_id, course_name, course_img_file):
	course_url = "https://meet.jit.si/cs%s" %course_id 
	em = EmailManager()
	text1 = "Dear %s %s,\n\nYou hav been successfully enrolled into the Course: %s." %(p_fname, p_lname, course_name)
	text = "Please use the below details to join this session as per the schedule:\n"
	text += "\n\t\tSchedule:\n\t\t\tDate: 11/10/2017\n\t\t\tStart Time: 2:00 PM PST"
	text += "\n\t\t\tEnd Time:  3:00 PM PST\n\t\t\tMeeting url: %s" %course_url
	text += "\n\nSee you in the classroom.\n\n"
	text += "Thanks,\nFood Craft Team\n"
	subj = "Enrollment to the course: %s" %course_name
	rcpnt = [p_email]
	em.send_email(subj, rcpnt, text1, text, course_img_file) 		
	

@app.route("/enroll", methods=['GET', 'POST'])
def enroll_student():
	data = request.json
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
