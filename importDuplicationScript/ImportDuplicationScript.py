import os
import pandas as pd

scriptDir = os.path.dirname(os.path.abspath(__file__))

#File name without extension
fileName = 'testDataExcel'
filePath = os.path.join(scriptDir, fileName)

class importObject:
    def __init__(self, 
                 firstPK=None, 
                 secondPK=None, 
                 thirdPK=None, 
                 fourthPK=None):
        
        self.firstPK = firstPK
        self.secondPK = secondPK
        self.thirdPK = thirdPK
        self.fourthPK = fourthPK

    def __str__(self):
        return (f"{self.firstPK}, {self.secondPK}, {self.thirdPK}, {self.fourthPK}")

    def __eq__(self, other):
        return self.firstPK == other.firstPK and self.secondPK == other.secondPK and self.thirdPK == other.thirdPK and self.fourthPK == other.fourthPK


def readFile(filePath):
    if filePath.endswith('.csv'):
        df = pd.read_csv(filePath, sep=';')
    elif filePath.endswith('.xlsx'):
        df = pd.read_excel(filePath)
    else:
        raise ValueError("File format not supported. Please provide a CSV or XLSX file.")
    return df

importObjectList = []
duplicationList = []

try:
    df = readFile(filePath + '.csv')
except Exception as e:
    try:
        df = readFile(filePath + '.xlsx')
    except Exception as ex:
        print(f"Error reading the file: {ex}")
        exit()

for index, row in df.iterrows():
    firstPKImport = row[0]
    if not pd.isna(firstPKImport):
        secondPKImport = row[3]
        thirdPKImport = row[5]
        fourthPKImport = row[8]
        newImportObject = importObject(firstPK=firstPKImport, secondPK=secondPKImport, 
            thirdPK=thirdPKImport, fourthPK=fourthPKImport)

        if newImportObject not in importObjectList:
            importObjectList.append(newImportObject)
        else:
            print("Object already in the list: ")
            print(newImportObject)
            duplicationList.append(newImportObject)

print(f"QTD. Objects: {len(importObjectList)} \nDuplicated objects: {len(duplicationList)}")

print("----------------------------- List of duplicated objects -----------------------------")
for duplicatedObj in duplicationList:
    print(duplicatedObj)