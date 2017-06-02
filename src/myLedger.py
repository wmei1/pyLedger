
#myLedger

import csv
import sqlite3
import sys
import os
import fileinput
import pickle
from category import *
import signal


id_num = 0
balance =None
CATE = ['Bank', 'Entertainment', 'Food', 'Other'] 
categories = ['Bank', 'Entertainment', 'Food','Other'] 
class myLedger:
	
	def init_db(self, cur):
		#Cols: Id, Name, Money, Date, Category, Descrip, Reconcile,
		cur.execute('''CREATE TABLE ledger (
		Id INT PRIMARY KEY NOT NULL,
		Name CHAR(50),
		Exc REAL,
		Date DATE,
		Cat CHAR(50),
		Desc CHAR(50))''')

	def insert_db(self, cur, csv):
		cur.execute("INSERT INTO ledger VALUES (?,?,?,?,?,?)", csv)

	def delete_db(self, cur, _id):
		cur.execute("DELETE from ledger where Id=?;", (_id,))
		
	def update_db(self, cur, csv):
		cur.execute ('''
			UPDATE ledger 
			SET Name = ?,
			Exc = ?,
			Date = ?,
			Cat = ?,
			Desc = ?,
			WHERE Id=?''', csv)

	def select_db(self, cur):
		cursor = cur.execute("SELECT * FROM ledger")
		print("ID|NAME|Money|Date|Category|Desc	")
		for row in cursor:
			print(row[0],"|",row[1],"|",row[2],"|",row[3],"|",row[4],"|",row[5])
		#print(cur.fetchall())

	def handler(self,signum, frame):
		global id_num
		with open('id_count.txt', 'w') as idCountFile:
			idCountFile.write(str(id_num))
		pickle.dump(category.categories,open('cate.p',"wb"))
		print("\nexiting")
		exit()

	def saveFiles(self):
		with open('save.txt', 'w') as saveFile:
			saveFile.write(str(id_num)+","+str(balance))

		pickle.dump(category.categories,open('cate.p',"wb"))

	def program(self, db, cur):
		global id_num, balance
		#global categories,CATE
		if balance == None:
			balance = float(input("Enter a starting balance."))
		signal.signal(signal.SIGTSTP, self.handler)
		while True:
			uinput = input("Main Menu, Enter h to show a list of commands: ")

			if uinput is "h":
				print('h - help text\n' 
				'p - prints out all entries in ledger\n'
				'b - modify the balance amount\n'
				'a - add a new entry\n' 
				'd - delete an entry\n' 
				'u - update an entry\n'
				'c - category options\n' 
				'q - quit program\n')

			if uinput is "p":
				print("Current Balance:"+str(balance))
				self.select_db(cur)

			if uinput is "b":
				try:
					balance = float(input("Enter a new balance: "))
				except ValueError:
					print("input was not a valid number");
					continue
			if uinput is "a":
				name = input("Enter the name:")
				exc = input("Enter Exchange amt(negatives for purchases, positive for deposits):")
				date = input("enter the date:")
				#prints out categories to choose from
				category.print_categories()
				cat = category.checkCategory()
				desc = input("enter a desc:")
				csv = (id_num,name,exc,date,cat,desc)
				id_num +=1
				#print(csv)
				self.insert_db(cur, csv)
				db.commit()
				balance += float(exc)

			if uinput is "d":
				self.select_db(cur)
				_id = int(input("Enter the id you wish to delete"))
				#amt = cur.execute("SELECT Exc from ledger where Id=?;", (_id,))
				#balance -= float(amt)
				self.delete_db(cur, _id)
				db.commit()

			if uinput is "u":
				_id = int(input("Enter the id you wish to update"))
				name = input("Enter the name:")
				exc = input("Enter Exchange amt:")
				date = input("enter the date:")
				cat = input("enter a category:")
				desc = input("enter a desc:")
				csv = (name,exc,date,cat,desc, _id)
				self.update_db(cur, csv)
				db.commit()

			if uinput is "c":
				category.main_category()

			if uinput is "q":
				return False
			
			self.saveFiles()

			
if __name__ == "__main__":

	idCountFile = None
	if (os.path.isfile('./save.txt')):
		with open('save.txt', 'r+') as saveFile:
			save = saveFile.readline()
			print(save)	#used for debeugging
			strSplit =save.split(",")
			id_num = int(strSplit[0])
			balance = float(strSplit[1])
	if (os.path.isfile('./cate.p')):
		category.categories = pickle.load( open("cate.p", "rb"))
		

	dbFlag = False
	dbFile = None
	if (not os.path.isfile('./ledger.db')):
		dbFile = open('ledger.db', 'w+')
		dbFile.close()
		dbFlag = True

	db = sqlite3.connect('ledger.db')
	cur = db.cursor()
	led = myLedger()

	if(dbFlag is True):
		led.init_db(cur)

	db.commit()
	led.program(db, cur)

	with open('save.txt', 'w') as saveFile:
		saveFile.write(str(id_num)+","+str(balance))

	pickle.dump(category.categories,open('cate.p',"wb"))
