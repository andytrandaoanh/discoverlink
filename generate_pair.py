import sys
from mysql_data import getWordList
from system_handler import writeListToFile, getWordFromTextFile


def getZERO_to_S_forms(wordForms, dictForms, outputDir):
	#get pairs like  CALF => CALVES

	pathOut = outputDir + "/ZERO_to_S_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		if (dictForm + 's' in wordForms):
			wordPairs.append(dictForm + ', ' + dictForm + 's')
			print ('finding...', dictForm)
	writeListToFile(wordPairs, pathOut)


def getS_to_ES_forms(wordForms, dictForms, outputDir):
	#get pairs like  CALF => CALVES

	pathOut = outputDir + "/S_to_ES_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		if (dictForm.endswith('s') and (dictForm + 'es' in wordForms)):
			wordPairs.append(dictForm + ', ' + dictForm + 'es')
			print ('finding...', dictForm)
	writeListToFile(wordPairs, pathOut)

def getX_to_ES_forms(wordForms, dictForms, outputDir):
	#get pairs like  CALF => CALVES

	pathOut = outputDir + "/X_to_ES_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		if (dictForm.endswith('x') and (dictForm + 'es' in wordForms)):
			wordPairs.append(dictForm + ', ' + dictForm + 'es')
			print ('finding...', dictForm)
	writeListToFile(wordPairs, pathOut)

def getSH_to_ES_forms(wordForms, dictForms, outputDir):
	#get pairs like  CALF => CALVES

	pathOut = outputDir + "/SH_to_ES_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		if (dictForm.endswith('sh') and (dictForm + 'es' in wordForms)):
			wordPairs.append(dictForm + ', ' + dictForm + 'es')
			print ('finding...', dictForm)
	writeListToFile(wordPairs, pathOut)

def getCH_to_ES_forms(wordForms, dictForms, outputDir):
	#get pairs like  CALF => CALVES

	pathOut = outputDir + "/CH_to_ES_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		if (dictForm.endswith('ch') and (dictForm + 'es' in wordForms)):
			wordPairs.append(dictForm + ', ' + dictForm + 'es')
			print ('finding...', dictForm)
	writeListToFile(wordPairs, pathOut)	

def getZ_to_ES_forms(wordForms, dictForms, outputDir):
	#get pairs like  CALF => CALVES

	pathOut = outputDir + "/Z_to_ES_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		if (dictForm.endswith('z') and (dictForm + 'es' in wordForms)):
			wordPairs.append(dictForm + ', ' + dictForm + 'es')
			print ('finding...', dictForm)
	writeListToFile(wordPairs, pathOut)	

def getE_to_ED_forms(wordForms, dictForms, outputDir):
	#get pairs like  CALF => CALVES

	pathOut = outputDir + "/E_to_ED_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		if (dictForm.endswith('e') and (dictForm + 'd' in wordForms)):
			wordPairs.append(dictForm + ', ' + dictForm + 'd')
			print ('finding...', dictForm)
	writeListToFile(wordPairs, pathOut)


def getF_to_VES_forms(wordForms, dictForms, outputDir):
	#get pairs like  CALF => CALVES

	pathOut = outputDir + "/F_to_VES_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		if (dictForm.endswith('f') and (dictForm[:-1] + 'ves') in wordForms):
			wordPairs.append(dictForm + ', ' + dictForm[:-1] + 'ves')
			print ('finding...', dictForm)

	writeListToFile(wordPairs, pathOut)

def get_FE_to_VES_forms(wordForms, dictForms, outputDir):
	#get pairs like  LIFE => LIVES

	pathOut = outputDir + "/FE_To_VES_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		if (dictForm.endswith('fe') and (dictForm[:-2] + 'ves') in wordForms):
			wordPairs.append(dictForm + ', ' + dictForm[:-2] + 'ves')
			print ('finding...', dictForm)

	writeListToFile(wordPairs, pathOut)

def get_Y_to_IES_forms(wordForms, dictForms, outputDir):
	#get pairs like  LIFE => LIVES

	pathOut = outputDir + "/Y_To_IES_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		if (dictForm.endswith('y') and (dictForm[:-1] + 'ies') in wordForms):
			wordPairs.append(dictForm + ', ' + dictForm[:-1] + 'ies')
			print ('finding...', dictForm)

	writeListToFile(wordPairs, pathOut)

def get_Y_to_IED_forms(wordForms, dictForms, outputDir):
	#get pairs like  LIFE => LIVES

	pathOut = outputDir + "/Y_To_IED_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		if (dictForm.endswith('y') and (dictForm[:-1] + 'ied') in wordForms):
			wordPairs.append(dictForm + ', ' + dictForm[:-1] + 'ied')
			print ('finding...', dictForm)

	writeListToFile(wordPairs, pathOut)

def get_D_to_DDED_forms(wordForms, dictForms, outputDir):
	#get pairs like  LIFE => LIVES

	pathOut = outputDir + "/D_To_DDED_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		if (dictForm.endswith('d') and (dictForm + 'ded') in wordForms):
			wordPairs.append(dictForm + ', ' + dictForm + 'ded')
			print ('finding...', dictForm)
	writeListToFile(wordPairs, pathOut)

def get_M_to_MMED_forms(wordForms, dictForms, outputDir):
	#get pairs like  LIFE => LIVES

	pathOut = outputDir + "/M_To_MMED_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		if (dictForm.endswith('m') and (dictForm + 'med') in wordForms):
			wordPairs.append(dictForm + ', ' + dictForm + 'med')
			print ('finding...', dictForm)
	writeListToFile(wordPairs, pathOut)

def get_N_to_NNED_forms(wordForms, dictForms, outputDir):
	#get pairs like  LIFE => LIVES

	pathOut = outputDir + "/N_To_NNED_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		if (dictForm.endswith('n') and (dictForm + 'ned') in wordForms):
			wordPairs.append(dictForm + ', ' + dictForm + 'ned')
			print ('finding...', dictForm)
	writeListToFile(wordPairs, pathOut)

def get_P_to_PPED_forms(wordForms, dictForms, outputDir):
	#get pairs like  LIFE => LIVES

	pathOut = outputDir + "/P_To_PPED_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		if (dictForm.endswith('p') and (dictForm + 'ped') in wordForms):
			wordPairs.append(dictForm + ', ' + dictForm + 'ped')
			print ('finding...', dictForm)
	writeListToFile(wordPairs, pathOut)

def get_R_to_RRED_forms(wordForms, dictForms, outputDir):
	#get pairs like  LIFE => LIVES

	pathOut = outputDir + "/R_To_RRED_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		if (dictForm.endswith('r') and (dictForm + 'red') in wordForms):
			wordPairs.append(dictForm + ', ' + dictForm + 'red')
			print ('finding...', dictForm)
	writeListToFile(wordPairs, pathOut)


def get_T_to_TTED_forms(wordForms, dictForms, outputDir):
	#get pairs like  LIFE => LIVES

	pathOut = outputDir + "/T_To_TTED_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		if (dictForm.endswith('t') and (dictForm + 'ted') in wordForms):
			wordPairs.append(dictForm + ', ' + dictForm + 'ted')
			print ('finding...', dictForm)
	writeListToFile(wordPairs, pathOut)


def get_E_to_ING_forms(wordForms, dictForms, outputDir):
	#get pairs like  LIFE => LIVES

	pathOut = outputDir + "/E_To_ING_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		if (dictForm.endswith('e') and (dictForm[:-1] + 'ing') in wordForms):
			wordPairs.append(dictForm + ', ' + dictForm[:-1] + 'ing')
			print ('finding...', dictForm)

def getZERO_to_ING_forms(wordForms, dictForms, outputDir):
	#get pairs like  CALF => CALVES

	pathOut = outputDir + "/ZERO_to_ING_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		if (dictForm + 'ing' in wordForms):
			wordPairs.append(dictForm + ', ' + dictForm + 'ing')
			print ('finding...', dictForm)
	writeListToFile(wordPairs, pathOut)

def get_D_to_DDING_forms(wordForms, dictForms, outputDir):
	#get pairs like  LIFE => LIVES

	pathOut = outputDir + "/D_To_DDING_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		if (dictForm.endswith('d') and (dictForm + 'ding') in wordForms):
			wordPairs.append(dictForm + ', ' + dictForm + 'ding')
			print ('finding...', dictForm)
	writeListToFile(wordPairs, pathOut)

def get_M_to_MMING_forms(wordForms, dictForms, outputDir):
	#get pairs like  LIFE => LIVES

	pathOut = outputDir + "/M_To_MMING_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		if (dictForm.endswith('m') and (dictForm + 'ming') in wordForms):
			wordPairs.append(dictForm + ', ' + dictForm + 'ming')
			print ('finding...', dictForm)
	writeListToFile(wordPairs, pathOut)

def get_N_to_NNING_forms(wordForms, dictForms, outputDir):
	#get pairs like  LIFE => LIVES

	pathOut = outputDir + "/N_To_NNING_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		if (dictForm.endswith('n') and (dictForm + 'ning') in wordForms):
			wordPairs.append(dictForm + ', ' + dictForm + 'ning')
			print ('finding...', dictForm)
	writeListToFile(wordPairs, pathOut)


def get_P_to_PPING_forms(wordForms, dictForms, outputDir):
	#get pairs like  LIFE => LIVES

	pathOut = outputDir + "/P_To_PPING_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		if (dictForm.endswith('p') and (dictForm + 'ping') in wordForms):
			wordPairs.append(dictForm + ', ' + dictForm + 'ping')
			print ('finding...', dictForm)
	writeListToFile(wordPairs, pathOut)


def get_R_to_RRING_forms(wordForms, dictForms, outputDir):
	#get pairs like  LIFE => LIVES

	pathOut = outputDir + "/R_To_RRING_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		if (dictForm.endswith('r') and (dictForm + 'ring') in wordForms):
			wordPairs.append(dictForm + ', ' + dictForm + 'ring')
			print ('finding...', dictForm)
	writeListToFile(wordPairs, pathOut)




def get_T_to_TTING_forms(wordForms, dictForms, outputDir):
	#get pairs like  LIFE => LIVES

	pathOut = outputDir + "/T_To_TTING_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		if (dictForm.endswith('t') and (dictForm + 'ting') in wordForms):
			wordPairs.append(dictForm + ', ' + dictForm + 'ting')
			print ('finding...', dictForm)
	writeListToFile(wordPairs, pathOut)


def extractWordPairs(standardDictPath, customDictPath, outputDir):
	pathIn = customDictPath
	pathDict = standardDictPath
	wordForms = getWordFromTextFile(pathIn)
	dictForms = getWordFromTextFile(pathDict)
	
	#S endings
	getZERO_to_S_forms(wordForms, dictForms, outputDir)
	getCH_to_ES_forms(wordForms, dictForms, outputDir)
	getSH_to_ES_forms(wordForms, dictForms, outputDir)
	getX_to_ES_forms(wordForms, dictForms, outputDir)
	getZ_to_ES_forms(wordForms, dictForms, outputDir)	
	getS_to_ES_forms(wordForms, dictForms, outputDir)
	getF_to_VES_forms(wordForms, dictForms, outputDir)
	get_Y_to_IES_forms(wordForms, dictForms, outputDir)
	getF_to_VES_forms(wordForms, dictForms, outputDir)
	get_FE_to_VES_forms(wordForms, dictForms, outputDir)
	
	#ED endings

	get_D_to_DDED_forms(wordForms, dictForms, outputDir)
	getE_to_ED_forms(wordForms, dictForms, outputDir)
	get_M_to_MMED_forms(wordForms, dictForms, outputDir)
	get_N_to_NNED_forms(wordForms, dictForms, outputDir)
	get_P_to_PPED_forms(wordForms, dictForms, outputDir)
	get_R_to_RRED_forms(wordForms, dictForms, outputDir)
	get_T_to_TTED_forms(wordForms, dictForms, outputDir)
	get_Y_to_IED_forms(wordForms, dictForms, outputDir)

	#ING endings
	get_E_to_ING_forms(wordForms, dictForms, outputDir)
	getZERO_to_ING_forms(wordForms, dictForms, outputDir)
	get_D_to_DDING_forms(wordForms, dictForms, outputDir)
	get_M_to_MMING_forms(wordForms, dictForms, outputDir)
	get_N_to_NNING_forms(wordForms, dictForms, outputDir)
	get_P_to_PPING_forms(wordForms, dictForms, outputDir)
	get_R_to_RRING_forms(wordForms, dictForms, outputDir)
	get_T_to_TTING_forms(wordForms, dictForms, outputDir)


