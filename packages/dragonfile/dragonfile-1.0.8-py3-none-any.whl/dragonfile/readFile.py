import csv

def readFile(self, indexColumn):
        columns = []

        with open(self.dFile, encoding=self.coding) as file:
            reader = csv.reader(file, delimiter=self.dSep)
            header = next(reader)
            nameColumn = header[indexColumn]

            for i, row in enumerate(reader):
                columns.append(row[indexColumn])

        dictDaux = {nameColumn: columns}
        self.dictD.update(dictDaux)

        if self.validate == True:
            print("Finish",indexColumn)
        
        indexColumn += 1

        return self.dictD, indexColumn