#! bin/python

import sqlite3 as lite

class DBManager():
	
	def __init__(self, db_store='sqlite3'):
		self.con = None
		if db_store == 'sqlite3':
			self.con = lite.connect('test.db')
		

	def execute_query(self, sql_qry_str, to_commit=True):	
		cur = None
		if self.con is not None:
			cur = self.con.cursor()
			cur.execute(sql_qry_str)
			if to_commit is True:
				self.con.commit()
			rows = cur.fetchall()

		return rows

	def check_if_table_exists(self, table_name):
		qry = "PRAGMA table_info([%s]);" %table_name
		rows = self.execute_query(qry)
		if rows == []:
			return False
		return True

	def fetch_all_rows(self, table_name):
		qry = "SELECT * from %s;" %table_name
		return self.execute_query(qry)

	def drop_table(self, table_name):
		#if self.check_if_table_exists(table_name) is True:
		qry = "DROP TABLE IF EXISTS %s;" %table_name
		self.execute_query(qry)

	def close(self):
		if self.con is not None:
			self.con.close()


	

