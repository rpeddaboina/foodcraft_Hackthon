#! ./bin/python

from db_manager import DBManager

dbManager = DBManager()

# Create User table
# Check whether that table exists already
if dbManager.check_if_table_exists('User') is False:
	qry = """CREATE TABLE User(Id INTEGER PRIMARY KEY, 
			First_Name TEXT, Last_Name TEXT, 
			Email_Id TEXT, Type SHORT);"""

	dbManager.execute_query(qry)

#Insert some Test data
# Check whether there are any existing rows in this table
if dbManager.fetch_all_rows('User') == []:
	user_list = [
		("Sridhar", "Kapilavai", "sridhar.ka79@gmail.com", 1),
		("Ramu", "Peddaboina", "sridhar.ka79@yahoo.com", 2),
	]
	for user in user_list:
		qry = '''INSERT INTO User(First_Name, Last_Name, Email_Id, Type) 
			VALUES ("%s", "%s", "%s", %d);''' %(user[0], user[1], user[2], user[3])
		dbManager.execute_query(qry)

# Create Courses table
# Check whether that table exists already
if dbManager.check_if_table_exists('Courses') is False:
        qry = """CREATE TABLE Courses(Id INTEGER PRIMARY KEY,
                        Name TEXT, Status INTEGER);"""
        dbManager.execute_query(qry)

#Insert some Test data
# Check whether there are any existing rows in this table
if dbManager.fetch_all_rows('Courses') == []:
        qry = """INSERT INTO Courses(Name, Status)
                VALUES ("Course-1", 1);"""
        dbManager.execute_query(qry)

# Create TrainingSessions table
# Check whether that table exists already
if dbManager.check_if_table_exists('TrainingSessions') is False:
        qry = """CREATE TABLE TrainingSessions(Id INTEGER PRIMARY KEY,
			Course_Id INTEGER, Capacity SHORT, Instructor_Id INTEGER, 
			Start_Time NUMERIC, End_Time NUMERIC, Status INTEGER);"""
        dbManager.execute_query(qry)

#Insert some Test data
# Check whether there are any existing rows in this table
if dbManager.fetch_all_rows('TrainingSessions') == []:
        qry = """INSERT INTO TrainingSessions(Course_Id, Capacity, Instructor_Id, 
			Start_Time, End_Time, Status)
                VALUES (1, 50, 1, 1509566400, 1509570000, 1);"""
        dbManager.execute_query(qry)

# Create SessionEnrollements table
# Check whether that table exists already
if dbManager.check_if_table_exists('SessionEnrollements') is False:
        qry = """CREATE TABLE SessionEnrollements(Id INTEGER PRIMARY KEY,
                        Training_Session_Id INTEGER, Student_Id INTEGER);"""
        dbManager.execute_query(qry)

#Insert some Test data
# Check whether there are any existing rows in this table
if dbManager.fetch_all_rows('SessionEnrollements') == []:
        qry = """INSERT INTO SessionEnrollements(Training_Session_Id, Student_Id)
                VALUES (1, 1);"""
        dbManager.execute_query(qry)




