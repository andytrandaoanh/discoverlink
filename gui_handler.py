import sys
from system_handler import openDir, getRawPath
from system_handler import loadFormatPairFile, writeListToFile
from generate_pair import extractWordPairs
from merge_pair import mergePairs, unpackPairs


#TAB 1 FUNCTIONS ================================
def processTab1(sDictPath, cDictPath, outputDir):
	#print('sDictPath:', sDictPath, '\ncDictPath:', cDictPath, '\noutputDir:', outputDir)
	extractWordPairs(sDictPath, cDictPath, outputDir)
	openDir(outputDir)
	sys.exit()


#TAB 2 FUNCTIONS ================================
def processTab2(dirIn, dirOut):
	#print('dirIn:', dirIn, '\ndirOut:', dirOut)
	mergePairs(dirIn, dirOut)
	openDir(dirOut)
	sys.exit()



#TAB 3 FUNCTIONS ================================
def processTab3(pathClean, dirRaw, dirRecycle):
	#print('pathClean:', pathClean, '\ndirRaw:', dirRaw, '\ndirRecycle:', dirRecycle)
	
	pathRaw = getRawPath(pathClean, dirRaw)
	pathRecycle = getRawPath(pathClean, dirRecycle)	

	#print('pathRaw', pathRaw)
	#print('\npathRecycle', pathRecycle)
	
	contentRaw = loadFormatPairFile(pathRaw)
	#print(contentRaw)
	contentClean = loadFormatPairFile(pathClean)
	#print(contentClean)

	recycleData = [item for item in contentRaw if item not in contentClean]
	
	dataOut = unpackPairs(recycleData)
	#print(dataOut)	

	writeListToFile(dataOut, pathRecycle)
	openDir(dirRecycle)
	sys.exit()
