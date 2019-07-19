import sys
from system_handler import openDir
from generate_pair import extractWordPairs
from merge_pair import mergePairs


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
def processTab3(dirClean, dirRaw, dirRecycle):
	print('dirClean:', dirClean, '\ndirRaw:', dirRaw, '\ndirRecycle:', dirRecycle)
	#mergePairs(dirIn, dirOut)
	#openDir(dirOut)
	#sys.exit()
