import sys
from mysql_data import getWordList
from system_handler import writeListToFile, getWordFromTextFile


pathIn = "E:/FULLTEXT/TEMPOUT/GENERAL_MATCHING_PAIRS.txt"
pathOut = "E:/FULLTEXT/SPECIALTY/GENERAL_MATCHING_PAIRS.txt"


wordPairs = getWordFromTextFile(pathIn)

newPairs = []

for pair in wordPairs:
	if(pair):
		items = pair.split(',')
		newPairs.append(items[0].strip() + ', ' + items[1].strip())


results = list( dict.fromkeys(newPairs))
results.sort()
#print(results)
writeListToFile(results, pathOut)