import sys
from mysql_data import getWordList
from system_handler import writeListToFile, getWordFromTextFile

def getCustomForms():
	wordForms = getWordList()
	lwordForms = [item.lower() for item in wordForms]
	pathOut = "E:/FULLTEXT/DICTIONARIES/Custom_Dictionary.txt"
	writeListToFile(lwordForms, pathOut)



def get_VES_forms(wordForms, dictForms):
	#get pairs like  CALF => CALVES

	pathOut = "E:/FULLTEXT/TEMPOUT/F_to_VES_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		if (dictForm.endswith('f') and (dictForm[:-1] + 'ves') in wordForms):
			wordPairs.append(dictForm + ', ' + dictForm[:-1] + 'ves')
			print ('finding...', dictForm)

	writeListToFile(wordPairs, pathOut)

def get_FE_to_VES_forms(wordForms, dictForms):
	#get pairs like  LIFE => LIVES

	pathOut = "E:/FULLTEXT/TEMPOUT/FE_To_VES_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		if (dictForm.endswith('fe') and (dictForm[:-2] + 'ves') in wordForms):
			wordPairs.append(dictForm + ', ' + dictForm[:-2] + 'ves')
			print ('finding...', dictForm)

	writeListToFile(wordPairs, pathOut)

def get_Y_to_IES_forms(wordForms, dictForms):
	#get pairs like  LIFE => LIVES

	pathOut = "E:/FULLTEXT/TEMPOUT/Y_To_IES_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		if (dictForm.endswith('y') and (dictForm[:-1] + 'ies') in wordForms):
			wordPairs.append(dictForm + ', ' + dictForm[:-1] + 'ies')
			print ('finding...', dictForm)

	writeListToFile(wordPairs, pathOut)

def get_Y_to_IED_forms(wordForms, dictForms):
	#get pairs like  LIFE => LIVES

	pathOut = "E:/FULLTEXT/TEMPOUT/Y_To_IED_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		if (dictForm.endswith('y') and (dictForm[:-1] + 'ied') in wordForms):
			wordPairs.append(dictForm + ', ' + dictForm[:-1] + 'ied')
			print ('finding...', dictForm)

	writeListToFile(wordPairs, pathOut)

def get_D_to_DDED_forms(wordForms, dictForms):
	#get pairs like  LIFE => LIVES

	pathOut = "E:/FULLTEXT/TEMPOUT/D_To_DDED_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		if (dictForm.endswith('d') and (dictForm + 'ded') in wordForms):
			wordPairs.append(dictForm + ', ' + dictForm + 'ded')
			print ('finding...', dictForm)
	writeListToFile(wordPairs, pathOut)

def get_M_to_MMED_forms(wordForms, dictForms):
	#get pairs like  LIFE => LIVES

	pathOut = "E:/FULLTEXT/TEMPOUT/M_To_MMED_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		if (dictForm.endswith('m') and (dictForm + 'med') in wordForms):
			wordPairs.append(dictForm + ', ' + dictForm + 'med')
			print ('finding...', dictForm)
	writeListToFile(wordPairs, pathOut)

def get_N_to_NNED_forms(wordForms, dictForms):
	#get pairs like  LIFE => LIVES

	pathOut = "E:/FULLTEXT/TEMPOUT/N_To_NNED_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		if (dictForm.endswith('n') and (dictForm + 'ned') in wordForms):
			wordPairs.append(dictForm + ', ' + dictForm + 'ned')
			print ('finding...', dictForm)
	writeListToFile(wordPairs, pathOut)

def get_P_to_PPED_forms(wordForms, dictForms):
	#get pairs like  LIFE => LIVES

	pathOut = "E:/FULLTEXT/TEMPOUT/P_To_PPED_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		if (dictForm.endswith('p') and (dictForm + 'ped') in wordForms):
			wordPairs.append(dictForm + ', ' + dictForm + 'ped')
			print ('finding...', dictForm)
	writeListToFile(wordPairs, pathOut)

def get_T_to_TTED_forms(wordForms, dictForms):
	#get pairs like  LIFE => LIVES

	pathOut = "E:/FULLTEXT/TEMPOUT/T_To_TTED_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		if (dictForm.endswith('t') and (dictForm + 'ted') in wordForms):
			wordPairs.append(dictForm + ', ' + dictForm + 'ted')
			print ('finding...', dictForm)
	writeListToFile(wordPairs, pathOut)

def extractWordPairs():
	pathIn = "E:/FULLTEXT/DICTIONARIES/Custom_Dictionary.txt"
	pathDict = "E:/FULLTEXT/DICTIONARIES/NLTK_Dictionary.txt"
	wordForms = getWordFromTextFile(pathIn)
	dictForms = getWordFromTextFile(pathDict)
	

	get_T_to_TTED_forms(wordForms, dictForms)

	




if __name__ == "__main__":
	extractWordPairs()