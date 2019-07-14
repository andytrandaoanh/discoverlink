from mysql_handler import upload_data
from system_handler import  getWordFromTextFile

if __name__ == "__main__":
	pathIn = "E:/FULLTEXT/CLEANMAP/Word_Pair_List_2019-07-14.txt"
	wordPairs = getWordFromTextFile(pathIn)

	dbData = []
	for item in wordPairs:
		if(item):
			pair = item.split(',')
			tup = (pair[0].strip(), pair[1].strip())
			dbData.append(tup)

	upload_data(dbData)
