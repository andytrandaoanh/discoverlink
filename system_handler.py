import os, sys

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


def getRawPath(pathIn, dirOut):
	JSON_EXTENSION = ".json"
	temp_path = pathIn
	temp_path = os.path.basename(temp_path)
	fname, fext = os.path.splitext(temp_path)
	pathOut =  os.path.join(dirOut, fname + JSON_EXTENSION) 
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