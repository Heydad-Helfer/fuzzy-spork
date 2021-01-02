from CardFileExtractor import CardFileExtractor

class CALFileExtractor(CardFileExtractor):
    def __init__(self, filename, cardID):
        CardFileExtractor.__init__(self, filename, "CAL", cardID)
        self.lines = [line.split('\t') for line in self.lines]
        self.lines = self.tuplify()

    def Sum(self):
        return sum(j for _, j in self.lines).__round__(2)

    #return a list of tuples of (date, deal-sum)
    def tuplify(self):
        count = 0
        newLines = []
        for line in self.lines:
            count += 1
            #drop title lines and sum line
            if count <= 3 or count == self.num_of_lines:
                continue

            #create a tuple of 
            colVal = (line[0], float(line[3].rstrip()))

            # print(colVal)
            newLines.append(colVal)
        
        return newLines