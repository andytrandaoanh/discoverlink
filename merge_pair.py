import sys
import system_handler as sysHandle
from mysql_data import getPairList 



def unpackPairs(pairList):
	outPairs = []
	for item in pairList:
		if(item):
			pairs = item.split('_')
			outPairs.append(pairs[0].strip() + ', ' + pairs[1].strip())
	return outPairs

def mergePairs(dirIn, dirOut):

	pathOut = sysHandle.getOutPath(dirOut)
	
	#print(pathOut)

	#print('dirIn:', dirIn)
	bigDict = sysHandle.loadWordPairs(dirIn)

	#print(bigDict)
	
	
	msqlList = getPairList()
	
	newDict = [item for item in bigDict if item not in msqlList]

	newPairList = unpackPairs(newDict)

	
	sysHandle.writeListToFile(newPairList, pathOut)

	
