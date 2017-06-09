import sqlite3
import sys
import os
import fileinput
import pickle
import signal
from category import *


class db:

	dbFile=None
	dbFlag=False
	conn = None
	cur = None
	dbname = None

	def __init__(self, dbname):
		self.dbname = dbname

	def create_db(self):
		cur.execute('CREATE TABLE '+dbname + ''' (
				ID INT PRIMARY KEY NOT NULL,
				NAME CHAR(20),
				AMT REAL,
				DATE DATE,
				CATE CHAR(50),
				DESC CHAR(50))''')

	def insert_row(self,csv):
		cur.execute("INSERT INTO "+dbname+" VALUES (?,?,?,?,?,?)", csv)

	def delete_row(self,_id):
		cur.execute("DELETE FROM "+dbname" WHERE ID=?",(_id,))

	def update_row(self, csv):
		cur.execute('UPDATE '+dbname+''' SET 
					NAME =?,
					EXC=?,
					DATE=?,
					CATE=?,
					DESC=?,
					WHERE ID=?''', csv)

	def print_db(self):
		cursor = cur.execute("SELECT * FROM "+dbname)
		print("ID|NAME|AMOUNT|DATE|CATEGORY|DESC")
		for row in cursor:
			print(row[0],"|",row[1],"|",row[2],"|",row[3],"|",row[4],"|",row[5])
		#print(cur.fetchall())

	def startConnection():
		dbFlag=False
		try:
			if(not os.path.isfile('./'+dbname+'.db')):
				dbFile = open(dbname+'.db', 'w+')
				dbFile.close()
				dbFlag = True
			conn = sqlite3.connection()
			cur=conn.cursor()
		except sqlite3.Error as er:
			print('er:',er.message)
		except IOError:
			print('No file found')

		return dbFlag

	def closeConnection():
		try:
			conn.close()
			dbFile.close()
			print('File and Connection Successfully Close')
		except IOError: 
			print("No file found")
		except sqlite3.Error as er:
			print('er:', er.message())


