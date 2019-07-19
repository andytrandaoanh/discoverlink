import os, sys
from datetime import date

def openDir(targetdir):
	#open directory when done	
	rpath = os.path.realpath(targetdir)
	os.startfile(rpath)


	
def readTextFile(filepath):
	try:
	    ofile = open(filepath, 'r', encoding = 'utf-8') 
	    data = ofile.read()
	    return data
	except FileNotFoundError:
	    print("file not found")    
	except Exception as e:
	    print(e)  


def getOutPath(dirOut):
	today = str(date.today())
	today = today.replace("-", "")
	fileName = "Word_Pair_List_" + today + ".txt"
	pathOut =  os.path.join(dirOut, fileName ) 
	return(pathOut)


def getWordFromTextFile(filepath):
    try:
        ofile = open(filepath, 'r', encoding = 'utf-8') 
        data = ofile.read()
        words = data.split('\n')
        return words

    except FileNotFoundError:
        print("file not found")    
    except Exception as e:
        print(e)    
        

def writeListToFile(vlist, vpath):
    with open(vpath, 'w', encoding ='utf-8') as file:
        for item in vlist:    
            file.write(item + "\n")



def fileToList(filepath):
    try:
        ofile = open(filepath, 'r', encoding = 'utf-8') 
        data = ofile.read()
        words = data.split('\n')
        return words
    except FileNotFoundError:
        print("file not found")    
    except Exception as e:
        print(e)    

def loadWordPairs(dirDic):
	dicFiles = os.listdir(dirDic)
	bigDic = []
	for fp in dicFiles:
		bigDic  += fileToList(os.path.join(dirDic, fp))

	dicData = list(dict.fromkeys(bigDic))
	dicData.sort()
	return formatData(dicData)


def formatData(dicData):
	outData = []
	for item in dicData:
		if(item):
			pairs = item.split(',')
			outData.append(pairs[0].strip()+ "_" + pairs[1].strip())
	return outData