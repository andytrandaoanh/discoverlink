import sys
import system_handler as sysHandle
from mysql_data import getPairList 
from datetime import date


def unpackPairs(pairList):
	outPairs = []
	for item in pairList:
		if(item):
			pairs = item.split('_')
			outPairs.append(pairs[0].strip() + ', ' + pairs[1].strip())
	return outPairs

def processText():

	dirIn = "E:/FULLTEXT/PAIR/TEMPOUT"
	#print(pathIn)
	dirOut = "E:/FULLTEXT/MAPPINGS"

	today = date.today()
	fileName = "Word_Pair_List_" + str(today) + ".txt"

	pathOut = "E:/FULLTEXT/MAPPINGS/" + fileName

	bigDict = sysHandle.loadWordPairs(dirIn)
	
	#print('bigDict', bigDict)
	msqlList = getPairList()
	#print('mySQL', msqlList)
	newDict = [item for item in bigDict if item not in msqlList]

	newPairList = unpackPairs(newDict)

	#print('new dictionary:', newPairList)
	sysHandle.writeListToFile(newPairList, pathOut)

	sysHandle.openDir(dirOut)
	sys.exit()
	


if __name__ == '__main__':
	processText()