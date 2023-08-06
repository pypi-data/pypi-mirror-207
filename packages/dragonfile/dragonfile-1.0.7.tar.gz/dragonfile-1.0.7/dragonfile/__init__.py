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
    
    def readFile(self):
        return readFile(self)

    def readFileSetPeriod(self, varOp0="", varOp1="Manhã", varOp2="Tarde", varOp3="Noite", varLog0="6", varLog1="12", varLog2="18", twoColumn=False):
        return readFileSetPeriod(self, varOp0=varOp0, varOp1=varOp1, varOp2=varOp2, varOp3=varOp3, varLog0=varLog0, varLog1=varLog1, varLog2=varLog2, twoColumn=twoColumn)

    def readFileRename(self, nameRow=[], renameRow=[], mode=False, varOp0=""):
        return readFileRename(self, nameRow=nameRow, renameRow=renameRow, mode=mode, varOp0=varOp0)
        
    def readValues(self):   
        return readValues(self)

    def fileToCsv(self):
        return fileToCsv(self)

    def lenColumns(self):
        return lenColumns(self)