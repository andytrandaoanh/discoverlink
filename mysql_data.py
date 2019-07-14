import mysql.connector
from mysql.connector import errorcode

def get_connection(dbname=''):
	try:
		connection = mysql.connector.connect(
		user='andyanh', password='DGandyanh#1234',
	    host='127.0.0.1', database = dbname)
		if connection.is_connected():
			return connection 
	except Error as e:
		return e


def formatWordList(records):
	wordList = []
	for word in records:
		wordList.append(word[0])	
	return wordList

def getWordList():
	DB_NAME = "lexicon"
	db = get_connection(DB_NAME)
	cursor = db.cursor()
	select_sql= ("select distinct word_form from words where book_id > 0")
	try:
		cursor.execute(select_sql)
		records = cursor.fetchall()
		return formatWordList(records)
	except Exception as e:
		print("Error encountered:", e)
	finally:
		cursor.close
		db.close


def formatPairList(records):
	wordList = []
	for item in records:
		wordList.append(item[0].strip() + '_' + item[1].strip())	
	return wordList


def getPairList():
	DB_NAME = "lexicon"
	db = get_connection(DB_NAME)
	cursor = db.cursor()
	select_sql= ("SELECT dict_form, word_form FROM  links")
	try:
		cursor.execute(select_sql)
		records = cursor.fetchall()
		#sreturn records
		return formatPairList(records)
	except Exception as e:
		print("Error encountered:", e)
	finally:
		cursor.close
		db.close
