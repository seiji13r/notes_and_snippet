import os
import json
import pprint
from pathlib import Path

def getAccessObj(scriptPath, dirLookUpName, fileLookUpName):
    scriptPath = Path(scriptPath)
    accessObj = dict()
    myFileAbsPath = None
    dirLookUpFound = False
    fileLookUpFound = False

    # downTopLevels = range(2)
    downTopLevels = [1,]

    for level in downTopLevels:
        searchPath = scriptPath.parents[level]
        newSearchPath = None
        print(f"Searching In: [{searchPath}]")
        for root, dirs, files in os.walk(searchPath):
            for lDir in dirs:
                if lDir == dirLookUpName:
                    newSearchPath = os.path.join(root, lDir)
                    print(f"Dir Located: {newSearchPath}")
                    dirLookUpFound = True
                    break
            if dirLookUpFound:
                break
        
    if dirLookUpFound:
        for root, dirs, files in os.walk(newSearchPath):
            for myFile in files:
                if myFile == fileLookUpName:
                    myFileAbsPath = os.path.join(root, myFile)
                    print(f"Access File Located: {myFileAbsPath}")
                    fileLookUpFound = True
                    break
            if fileLookUpFound:
                break
    
    if fileLookUpFound:
        with open(myFileAbsPath, 'r') as jsonFileObj:
            accessObj = json.load(jsonFileObj)


    return accessObj

if __name__ == "__main__":

    thisPath = os.path.dirname(os.path.abspath(__file__))
    credObj = getAccessObj(thisPath, "_private", "paramikoTestServ.json")
    pprint.pprint(credObj)