import csv

def readFileSetPeriod(self, indexColumn, varOp0="", varOp1="Manhã", varOp2="Tarde", varOp3="Noite", varLog0="6", varLog1="12", varLog2="18", twoColumn=False):
        columns = []
        columnsTwo = []

        with open(self.dFile, encoding=self.coding) as file:
            reader = csv.reader(file, delimiter=self.dSep)
            header = next(reader)
            nameColumn = header[indexColumn]
            extraColum = "New"+header[indexColumn]
            
            for i, row in enumerate(reader):
                word = row[indexColumn]

                if word != "":
                    word = int(word[0]+word[1])
                else:
                    word = varOp0

                if word != varOp0 :

                    if word > varLog0 and word <= varLog1:
                        word = varOp1

                    elif word > varLog1 and word < varLog2:
                        word = varOp2

                    else:
                        word = varOp3
                        
                else:
                    pass
                
                columns.append(word)
                columnsTwo.append(row[indexColumn])

            if twoColumn == False:
                dictDaux = {extraColum: columns}
                self.dictD.update(dictDaux)

                if self.validate == True:
                    print("Finish",indexColumn)

                indexColumn += 1
            else:
                dictDaux1 = {nameColumn: columnsTwo}
                dictDaux2 = {extraColum: columns}

                dictDaux1.update(dictDaux2)
                self.dictD.update(dictDaux1)

                if self.validate == True:
                    print("Finish",indexColumn)

                indexColumn += 1
            
            return self.dictD, indexColumn