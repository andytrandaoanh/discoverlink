import sys
from mysql_data import getWordList
from system_handler import writeListToFile, getWordFromTextFile


def getZERO_to_S_forms(wordForms, dictForms, outputDir):
	#get pairs like  CALF => CALVES

	pathOut = outputDir + "/ZERO_to_S_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		inflection = dictForm + 's'
		if (inflection in wordForms):
			wordPairs.append(dictForm + ', ' + inflection)
			print ('finding...', dictForm, ', ', inflection)
	writeListToFile(wordPairs, pathOut)


def getS_to_ES_forms(wordForms, dictForms, outputDir):
	#get pairs like  CALF => CALVES

	pathOut = outputDir + "/S_to_ES_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		inflection = dictForm + 'es'
		if (dictForm.endswith('s') and inflection in wordForms):
			wordPairs.append(dictForm + ', ' + inflection)
			print ('finding...', dictForm, ', ', inflection)
	writeListToFile(wordPairs, pathOut)

def getX_to_ES_forms(wordForms, dictForms, outputDir):
	#get pairs like  CALF => CALVES

	pathOut = outputDir + "/X_to_ES_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		inflection = dictForm + 'es'
		if (dictForm.endswith('x') and inflection in wordForms):
			wordPairs.append(dictForm + ', ' + inflection)
			print ('finding...', dictForm, ', ', inflection)
	writeListToFile(wordPairs, pathOut)

def getSH_to_ES_forms(wordForms, dictForms, outputDir):
	#get pairs like  CALF => CALVES

	pathOut = outputDir + "/SH_to_ES_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		inflection = dictForm + 'es'
		if (dictForm.endswith('sh') and inflection in wordForms):
			wordPairs.append(dictForm + ', ' + inflection)
			print ('finding...', dictForm, ', ', inflection)
	writeListToFile(wordPairs, pathOut)

def getCH_to_ES_forms(wordForms, dictForms, outputDir):
	#get pairs like  CALF => CALVES

	pathOut = outputDir + "/CH_to_ES_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		inflection = dictForm + 'es'
		if (dictForm.endswith('ch') and inflection in wordForms):
			wordPairs.append(dictForm + ', ' + inflection)
			print ('finding...', dictForm, ', ', inflection)
	writeListToFile(wordPairs, pathOut)	

def getZ_to_ES_forms(wordForms, dictForms, outputDir):
	#get pairs like  CALF => CALVES

	pathOut = outputDir + "/Z_to_ES_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		inflection = dictForm + 'es'
		if (dictForm.endswith('z') and inflection in wordForms):
			wordPairs.append(dictForm + ', ' + inflection)
			print ('finding...', dictForm, ', ', inflection)
	writeListToFile(wordPairs, pathOut)	


def getF_to_VES_forms(wordForms, dictForms, outputDir):
	#get pairs like  CALF => CALVES

	pathOut = outputDir + "/F_to_VES_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		inflection = dictForm[:-1] + 'ves'
		if (dictForm.endswith('f') and inflection in wordForms):
			wordPairs.append(dictForm + ', ' + inflection)
			print ('finding...', dictForm, ', ', inflection)

	writeListToFile(wordPairs, pathOut)

def get_FE_to_VES_forms(wordForms, dictForms, outputDir):
	#get pairs like  LIFE => LIVES

	pathOut = outputDir + "/FE_To_VES_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		inflection = dictForm[:-2] + 'ves'
		if (dictForm.endswith('fe') and inflection in wordForms):
			wordPairs.append(dictForm + ', ' + inflection)
			print ('finding...', dictForm, ', ', inflection)

	writeListToFile(wordPairs, pathOut)

def get_Y_to_IES_forms(wordForms, dictForms, outputDir):
	#get pairs like  LIFE => LIVES

	pathOut = outputDir + "/Y_To_IES_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		inflection = dictForm[:-1] + 'ies'
		if (dictForm.endswith('y') and inflection in wordForms):
			wordPairs.append(dictForm + ', ' + inflection)
			print ('finding...', dictForm, ', ', inflection)

	writeListToFile(wordPairs, pathOut)

def get_D_to_DDED_forms(wordForms, dictForms, outputDir):
	#get pairs like  LIFE => LIVES

	pathOut = outputDir + "/D_To_DDED_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		inflection = dictForm + 'ded'
		if (dictForm.endswith('d') and inflection in wordForms):
			wordPairs.append(dictForm + ', ' + inflection)
			print ('finding...', dictForm, ', ', inflection)
	writeListToFile(wordPairs, pathOut)

def getE_to_ED_forms(wordForms, dictForms, outputDir):
	#get pairs like  CALF => CALVES

	pathOut = outputDir + "/E_to_ED_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		inflection = dictForm + 'd'
		if (dictForm.endswith('e') and (inflection in wordForms)):
			wordPairs.append(dictForm + ', ' + inflection)
			print ('finding...', dictForm, ', ', inflection)
	writeListToFile(wordPairs, pathOut)



def get_L_to_LLED_forms(wordForms, dictForms, outputDir):
	#get pairs like  LIFE => LIVES

	pathOut = outputDir + "/L_To_LLED_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		inflection = dictForm + 'lled'
		if (dictForm.endswith('l') and inflection in wordForms):
			wordPairs.append(dictForm + ', ' + inflection)
			print ('finding...', dictForm, ', ', inflection)
	writeListToFile(wordPairs, pathOut)

def get_M_to_MMED_forms(wordForms, dictForms, outputDir):
	#get pairs like  LIFE => LIVES

	pathOut = outputDir + "/M_To_MMED_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		inflection = dictForm + 'med'
		if (dictForm.endswith('m') and inflection in wordForms):
			wordPairs.append(dictForm + ', ' + inflection)
			print ('finding...', dictForm, ', ', inflection)
	writeListToFile(wordPairs, pathOut)

def get_N_to_NNED_forms(wordForms, dictForms, outputDir):
	#get pairs like  LIFE => LIVES

	pathOut = outputDir + "/N_To_NNED_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		inflection = dictForm + 'ned'
		if (dictForm.endswith('n') and inflection in wordForms):
			wordPairs.append(dictForm + ', ' + inflection)
			print ('finding...', dictForm, ', ', inflection)
	writeListToFile(wordPairs, pathOut)

def get_P_to_PPED_forms(wordForms, dictForms, outputDir):
	#get pairs like  LIFE => LIVES

	pathOut = outputDir + "/P_To_PPED_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		inflection = dictForm + 'ped'
		if (dictForm.endswith('p') and inflection in wordForms):
			wordPairs.append(dictForm + ', ' + inflection)
			print ('finding...', dictForm, ', ', inflection)
	writeListToFile(wordPairs, pathOut)

def get_R_to_RRED_forms(wordForms, dictForms, outputDir):
	#get pairs like  LIFE => LIVES

	pathOut = outputDir + "/R_To_RRED_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		inflection = dictForm + 'red'
		if (dictForm.endswith('r') and inflection in wordForms):
			wordPairs.append(dictForm + ', ' + inflection)
			print ('finding...', dictForm, ', ', inflection)
	writeListToFile(wordPairs, pathOut)


def get_T_to_TTED_forms(wordForms, dictForms, outputDir):
	#get pairs like  LIFE => LIVES

	pathOut = outputDir + "/T_To_TTED_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		inflection = dictForm + 'ted'
		if (dictForm.endswith('t') and inflection in wordForms):
			wordPairs.append(dictForm + ', ' + inflection)
			print ('finding...', dictForm, ', ', inflection)
	writeListToFile(wordPairs, pathOut)

def get_Y_to_IED_forms(wordForms, dictForms, outputDir):
	#get pairs like  LIFE => LIVES

	pathOut = outputDir + "/Y_To_IED_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		inflection = dictForm[:-1] + 'ied'
		if (dictForm.endswith('y') and inflection in wordForms):
			wordPairs.append(dictForm + ', ' + inflection)
			print ('finding...', dictForm, ', ', inflection)

	writeListToFile(wordPairs, pathOut)



def get_E_to_ING_forms(wordForms, dictForms, outputDir):
	#get pairs like  LIFE => LIVES

	pathOut = outputDir + "/E_To_ING_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		inflection = dictForm[:-1] + 'ing'
		if (dictForm.endswith('e') and inflection in wordForms):
			wordPairs.append(dictForm + ', ' + inflection)
			print ('finding...', dictForm, ', ', inflection)
	
	writeListToFile(wordPairs, pathOut)


def get_IE_to_YNG_forms(wordForms, dictForms, outputDir):
	#get pairs like  LIFE => LIVES

	pathOut = outputDir + "/IE_To_YNG_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		if(len(dictForm) > 2):
			inflection = dictForm[:-2] + 'yng'
			if (dictForm.endswith('ie') and inflection in wordForms):
				wordPairs.append(dictForm + ', ' + inflection)
				print ('finding...', dictForm, ', ', inflection)
	writeListToFile(wordPairs, pathOut)

def getZERO_to_ING_forms(wordForms, dictForms, outputDir):
	#get pairs like  CALF => CALVES

	pathOut = outputDir + "/ZERO_to_ING_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		inflection = dictForm + 'ing'
		if (inflection in wordForms):
			wordPairs.append(dictForm + ', ' + inflection)
			print ('finding...', dictForm, ', ', inflection)
	writeListToFile(wordPairs, pathOut)

def get_D_to_DDING_forms(wordForms, dictForms, outputDir):
	#get pairs like  LIFE => LIVES

	pathOut = outputDir + "/D_To_DDING_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		inflection = dictForm + 'ding'
		if (dictForm.endswith('d') and inflection in wordForms):
			wordPairs.append(dictForm + ', ' + inflection)
			print ('finding...', dictForm, ', ', inflection)
	writeListToFile(wordPairs, pathOut)


def get_L_to_LLING_forms(wordForms, dictForms, outputDir):
	#get pairs like  LIFE => LIVES

	pathOut = outputDir + "/L_To_LLING_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		inflection = dictForm + 'ling'
		if (dictForm.endswith('l') and inflection in wordForms):
			wordPairs.append(dictForm + ', ' + inflection)
			print ('finding...', dictForm, ', ', inflection)
	writeListToFile(wordPairs, pathOut)


def get_M_to_MMING_forms(wordForms, dictForms, outputDir):
	#get pairs like  LIFE => LIVES

	pathOut = outputDir + "/M_To_MMING_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		inflection = dictForm + 'ming'
		if (dictForm.endswith('m') and inflection in wordForms):
			wordPairs.append(dictForm + ', ' + inflection)
			print ('finding...', dictForm, ', ', inflection)
	writeListToFile(wordPairs, pathOut)

def get_N_to_NNING_forms(wordForms, dictForms, outputDir):
	#get pairs like  LIFE => LIVES

	pathOut = outputDir + "/N_To_NNING_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		inflection = dictForm + 'ning'
		if (dictForm.endswith('n') and inflection in wordForms):
			wordPairs.append(dictForm + ', ' + inflection)
			print ('finding...', dictForm, ', ', inflection)
	writeListToFile(wordPairs, pathOut)


def get_P_to_PPING_forms(wordForms, dictForms, outputDir):
	#get pairs like  LIFE => LIVES

	pathOut = outputDir + "/P_To_PPING_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		inflection = dictForm + 'ping'
		if (dictForm.endswith('p') and inflection in wordForms):
			wordPairs.append(dictForm + ', ' + inflection)
			print ('finding...', dictForm, ', ', inflection)
	writeListToFile(wordPairs, pathOut)


def get_R_to_RRING_forms(wordForms, dictForms, outputDir):
	#get pairs like  LIFE => LIVES

	pathOut = outputDir + "/R_To_RRING_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		inflection = dictForm + 'ring'
		if (dictForm.endswith('r') and inflection in wordForms):
			wordPairs.append(dictForm + ', ' + inflection)
			print ('finding...', dictForm, ', ', inflection)
	writeListToFile(wordPairs, pathOut)




def get_T_to_TTING_forms(wordForms, dictForms, outputDir):
	#get pairs like  LIFE => LIVES

	pathOut = outputDir + "/T_To_TTING_Match_Pairs.txt"

	wordPairs = []
	for dictForm in dictForms:
		inflection = dictForm + 'ting'
		if (dictForm.endswith('t') and inflection in wordForms):
			wordPairs.append(dictForm + ', ' + inflection)
			print ('finding...', dictForm, ', ', inflection)
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
	get_L_to_LLED_forms(wordForms, dictForms, outputDir)
	get_M_to_MMED_forms(wordForms, dictForms, outputDir)
	get_N_to_NNED_forms(wordForms, dictForms, outputDir)
	get_P_to_PPED_forms(wordForms, dictForms, outputDir)
	get_R_to_RRED_forms(wordForms, dictForms, outputDir)
	get_T_to_TTED_forms(wordForms, dictForms, outputDir)
	get_Y_to_IED_forms(wordForms, dictForms, outputDir)

	#ING endings
	getZERO_to_ING_forms(wordForms, dictForms, outputDir)
	get_E_to_ING_forms(wordForms, dictForms, outputDir)
	get_IE_to_YNG_forms(wordForms, dictForms, outputDir)
	get_D_to_DDING_forms(wordForms, dictForms, outputDir)
	get_L_to_LLING_forms(wordForms, dictForms, outputDir)
	get_M_to_MMING_forms(wordForms, dictForms, outputDir)
	get_N_to_NNING_forms(wordForms, dictForms, outputDir)
	get_P_to_PPING_forms(wordForms, dictForms, outputDir)
	get_R_to_RRING_forms(wordForms, dictForms, outputDir)
	get_T_to_TTING_forms(wordForms, dictForms, outputDir)


