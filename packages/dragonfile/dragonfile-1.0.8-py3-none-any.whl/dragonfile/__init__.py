from .readFile import readFile
from .readFileSetPeriod import readFileSetPeriod
from .readFileRename import readFileRename
from .readValues import readValues
from .fileToCsv import fileToCsv
from .lenColumns import lenColumns

class SetFile:
    def __init__ (self, dFile, dSep=",", coding="utf-8", dictD={}, validate=False):
        self.dFile = dFile
        self.dSep = dSep
        self.coding = coding
        self.dictD = dictD
        self.validate = validate
    
    def readFile(self, indexColumn):
        return readFile(self, indexColumn=indexColumn)

    def readFileSetPeriod(self, indexColumn, varOp0="", varOp1="Manhã", varOp2="Tarde", varOp3="Noite", varLog0="6", varLog1="12", varLog2="18", twoColumn=False):
        return readFileSetPeriod(self, indexColumn=indexColumn, varOp0=varOp0, varOp1=varOp1, varOp2=varOp2, varOp3=varOp3, varLog0=varLog0, varLog1=varLog1, varLog2=varLog2, twoColumn=twoColumn)

    def readFileRename(self, indexColumn, nameRow=[], renameRow=[], mode=False, varOp0=""):
        return readFileRename(self, indexColumn=indexColumn ,nameRow=nameRow, renameRow=renameRow, mode=mode, varOp0=varOp0)
        
    def readValues(self, indexColumn):   
        return readValues(self, indexColumn=indexColumn)

    def fileToCsv(self, indexColumn):
        return fileToCsv(self, indexColumn=indexColumn)

    def lenColumns(self, indexColumn):
        return lenColumns(self, indexColumn=indexColumn)