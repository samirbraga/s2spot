# -*- coding: utf-8 -*- 
import pyodbc

class DBController:
	cnxn = None
	cursor = None

	@classmethod
	def connect(self, database, server, user, password):
		auth = ""
		if user and password:
			auth += "user=%s" % (user) 
			auth += "pass=%s" % (password)
		else:
			auth += "Trusted_Connection=yes"

		DBController.cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};" +
		                      "Server=%s;" % (server) +
		                      "Database=%s;" % (database) +
							  auth)
		DBController.cursor = DBController.cnxn.cursor()

	@classmethod
	def execute(self, query):
		DBController.cursor.execute(query)

	@classmethod
	def get(self):
		return DBController.cursor