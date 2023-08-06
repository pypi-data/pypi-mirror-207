import csv

def readFileRename(self, indexColumn, nameRow=[], renameRow=[], mode=False, varOp0=""):
        columns = []

        with open(self.dFile, encoding=self.coding) as file:
            reader = csv.reader(file, delimiter=self.dSep)
            header = next(reader)
            nameColumn = header[indexColumn]

            for row in reader:
                if mode == False:
                    if row[indexColumn] in nameRow:
                        index = nameRow.index(row[indexColumn])
                        columns.append(renameRow[index])
                    else:
                        columns.append(row[indexColumn])
                else:
                    if row[indexColumn] in nameRow:
                        index = nameRow.index(row[indexColumn])
                        columns.append(renameRow[index])
                    else:
                        columns.append(varOp0)

            dictDaux = {nameColumn: columns}
            self.dictD.update(dictDaux)

            if self.validate == True:
                    print("Finish",indexColumn)

            indexColumn += 1

            return self.dictD, indexColumn