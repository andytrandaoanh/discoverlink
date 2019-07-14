import sys
from mysql_data import getWordList
from system_handler import writeListToFile, getWordFromTextFile

def getCustomForms():
	wordForms = getWordList()
	lwordForms = [item.lower() for item in wordForms]
	pathOut = "E:/FULLTEXT/DICTIONARIES/Custom_Dictionary.txt"
	writeListToFile(lwordForms, pathOut)


def getZERO_to_S_forms(wordForms, dictForms):
	#get pairs like  CALF => CALVES

	pathOut = "E:/FULLTEXT/TEMPOUT/ZERO_to_S_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		if (dictForm + 's' in wordForms):
			wordPairs.append(dictForm + ', ' + dictForm + 's')
			print ('finding...', dictForm)
	writeListToFile(wordPairs, pathOut)


def getS_to_ES_forms(wordForms, dictForms):
	#get pairs like  CALF => CALVES

	pathOut = "E:/FULLTEXT/TEMPOUT/S_to_ES_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		if (dictForm.endswith('s') and (dictForm + 'es' in wordForms)):
			wordPairs.append(dictForm + ', ' + dictForm + 'es')
			print ('finding...', dictForm)
	writeListToFile(wordPairs, pathOut)

def getX_to_ES_forms(wordForms, dictForms):
	#get pairs like  CALF => CALVES

	pathOut = "E:/FULLTEXT/TEMPOUT/X_to_ES_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		if (dictForm.endswith('x') and (dictForm + 'es' in wordForms)):
			wordPairs.append(dictForm + ', ' + dictForm + 'es')
			print ('finding...', dictForm)
	writeListToFile(wordPairs, pathOut)

def getSH_to_ES_forms(wordForms, dictForms):
	#get pairs like  CALF => CALVES

	pathOut = "E:/FULLTEXT/TEMPOUT/SH_to_ES_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		if (dictForm.endswith('sh') and (dictForm + 'es' in wordForms)):
			wordPairs.append(dictForm + ', ' + dictForm + 'es')
			print ('finding...', dictForm)
	writeListToFile(wordPairs, pathOut)

def getCH_to_ES_forms(wordForms, dictForms):
	#get pairs like  CALF => CALVES

	pathOut = "E:/FULLTEXT/TEMPOUT/CH_to_ES_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		if (dictForm.endswith('ch') and (dictForm + 'es' in wordForms)):
			wordPairs.append(dictForm + ', ' + dictForm + 'es')
			print ('finding...', dictForm)
	writeListToFile(wordPairs, pathOut)	

def getZ_to_ES_forms(wordForms, dictForms):
	#get pairs like  CALF => CALVES

	pathOut = "E:/FULLTEXT/TEMPOUT/Z_to_ES_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		if (dictForm.endswith('z') and (dictForm + 'es' in wordForms)):
			wordPairs.append(dictForm + ', ' + dictForm + 'es')
			print ('finding...', dictForm)
	writeListToFile(wordPairs, pathOut)	

def getE_to_ED_forms(wordForms, dictForms):
	#get pairs like  CALF => CALVES

	pathOut = "E:/FULLTEXT/TEMPOUT/E_to_ED_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		if (dictForm.endswith('e') and (dictForm + 'd' in wordForms)):
			wordPairs.append(dictForm + ', ' + dictForm + 'd')
			print ('finding...', dictForm)
	writeListToFile(wordPairs, pathOut)


def getF_to_VES_forms(wordForms, dictForms):
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


def get_E_to_ING_forms(wordForms, dictForms):
	#get pairs like  LIFE => LIVES

	pathOut = "E:/FULLTEXT/TEMPOUT/E_To_ING_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		if (dictForm.endswith('e') and (dictForm[:-1] + 'ing') in wordForms):
			wordPairs.append(dictForm + ', ' + dictForm[:-1] + 'ing')
			print ('finding...', dictForm)

def getZERO_to_ING_forms(wordForms, dictForms):
	#get pairs like  CALF => CALVES

	pathOut = "E:/FULLTEXT/TEMPOUT/ZERO_to_ING_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		if (dictForm + 'ing' in wordForms):
			wordPairs.append(dictForm + ', ' + dictForm + 'ing')
			print ('finding...', dictForm)
	writeListToFile(wordPairs, pathOut)

def get_D_to_DDING_forms(wordForms, dictForms):
	#get pairs like  LIFE => LIVES

	pathOut = "E:/FULLTEXT/TEMPOUT/D_To_DDING_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		if (dictForm.endswith('d') and (dictForm + 'ding') in wordForms):
			wordPairs.append(dictForm + ', ' + dictForm + 'ding')
			print ('finding...', dictForm)
	writeListToFile(wordPairs, pathOut)

def get_M_to_MMING_forms(wordForms, dictForms):
	#get pairs like  LIFE => LIVES

	pathOut = "E:/FULLTEXT/TEMPOUT/M_To_MMING_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		if (dictForm.endswith('m') and (dictForm + 'ming') in wordForms):
			wordPairs.append(dictForm + ', ' + dictForm + 'ming')
			print ('finding...', dictForm)
	writeListToFile(wordPairs, pathOut)

def get_N_to_NNING_forms(wordForms, dictForms):
	#get pairs like  LIFE => LIVES

	pathOut = "E:/FULLTEXT/TEMPOUT/N_To_NNING_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		if (dictForm.endswith('n') and (dictForm + 'ning') in wordForms):
			wordPairs.append(dictForm + ', ' + dictForm + 'ning')
			print ('finding...', dictForm)
	writeListToFile(wordPairs, pathOut)


def get_P_to_PPING_forms(wordForms, dictForms):
	#get pairs like  LIFE => LIVES

	pathOut = "E:/FULLTEXT/TEMPOUT/P_To_PPING_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		if (dictForm.endswith('p') and (dictForm + 'ping') in wordForms):
			wordPairs.append(dictForm + ', ' + dictForm + 'ping')
			print ('finding...', dictForm)
	writeListToFile(wordPairs, pathOut)
def get_T_to_TTING_forms(wordForms, dictForms):
	#get pairs like  LIFE => LIVES

	pathOut = "E:/FULLTEXT/TEMPOUT/T_To_TTING_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		if (dictForm.endswith('t') and (dictForm + 'ting') in wordForms):
			wordPairs.append(dictForm + ', ' + dictForm + 'ting')
			print ('finding...', dictForm)
	writeListToFile(wordPairs, pathOut)


def extractWordPairs():
	pathIn = "E:/FULLTEXT/DICTIONARIES/Custom_Dictionary.txt"
	pathDict = "E:/FULLTEXT/DICTIONARIES/NLTK_Dictionary.txt"
	wordForms = getWordFromTextFile(pathIn)
	dictForms = getWordFromTextFile(pathDict)
	
	#S endings
	#getZERO_to_S_forms(wordForms, dictForms)
	#getCH_to_ES_forms(wordForms, dictForms)
	#getSH_to_ES_forms(wordForms, dictForms)
	#getX_to_ES_forms(wordForms, dictForms)
	#getZ_to_ES_forms(wordForms, dictForms)	
	#getS_to_ES_forms(wordForms, dictForms)
	#getF_to_VES_forms(wordForms, dictForms)
	#get_Y_to_IES_forms(wordForms, dictForms)
	#getF_to_VES_forms(wordForms, dictForms)
	#get_FE_to_VES_forms(wordForms, dictForms)
	
	#ED endings

	#get_D_to_DDED_forms(wordForms, dictForms)
	#getE_to_ED_forms(wordForms, dictForms)
	#get_M_to_MMED_forms(wordForms, dictForms)
	#get_N_to_NNED_forms(wordForms, dictForms)
	#get_P_to_PPED_forms(wordForms, dictForms)
	#get_T_to_TTED_forms(wordForms, dictForms)
	#get_Y_to_IED_forms(wordForms, dictForms)

	#ING endings
	get_E_to_ING_forms(wordForms, dictForms)
	getZERO_to_ING_forms(wordForms, dictForms)
	get_D_to_DDING_forms(wordForms, dictForms)
	get_M_to_MMING_forms(wordForms, dictForms)
	get_N_to_NNING_forms(wordForms, dictForms)
	get_P_to_PPING_forms(wordForms, dictForms)
	get_T_to_TTING_forms(wordForms, dictForms)


if __name__ == "__main__":
	extractWordPairs()