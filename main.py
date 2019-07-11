import sys
from mysql_data import getWordList
from system_handler import writeListToFile, getWordFromTextFile

def getCustomForms():
	wordForms = getWordList()
	lwordForms = [item.lower() for item in wordForms]
	pathOut = "E:/FULLTEXT/DICTIONARIES/Custom_Dictionary.txt"
	writeListToFile(lwordForms, pathOut)



def extractWordPairs():
	pathIn = "E:/FULLTEXT/DICTIONARIES/Custom_Dictionary.txt"
	pathDict = "E:/FULLTEXT/DICTIONARIES/NLTK_Dictionary.txt"
	wordForms = getWordFromTextFile(pathIn)
	dictForms = getWordFromTextFile(pathDict)
	
	FACTOR = 'ring'

	pathOut = "E:/FULLTEXT/TEMPOUT/"+ FACTOR.upper() + "_Match_Pairs.txt"
	#pathOut = "E:/FULLTEXT/TEMPOUT/ING_2_Match_Pairs.txt"

	wordPairs = []
	#run S for plural and present test
	for df in dictForms:
		if (df + FACTOR) in wordForms:
			wordPairs.append(df + ', ' + df + FACTOR)
			print ('finding...', df)
	

	writeListToFile(wordPairs, pathOut)




if __name__ == "__main__":
	extractWordPairs()