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

def mergePairs(dirIn, dirOut, dirRecycle):

	pathOut = sysHandle.getOutPath(dirOut)
	
	#print(pathOut)

	#print('dirIn:', dirIn)
	bigDict = sysHandle.loadWordPairs(dirIn)

	#print(bigDict)
	
	recycleList = sysHandle.loadWordPairs(dirRecycle)	
	#print(recycleList)
	
	msqlList = getPairList()
	
	newDict = [item for item in bigDict if item not in msqlList]

	outDict = [item for item in newDict if item not in recycleList]	

	newPairList = unpackPairs(outDict)

	
	sysHandle.writeListToFile(newPairList, pathOut)

	
