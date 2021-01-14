import pandas as pd

class CardFileExtractor:
    def __init__(self, filename, cardVendor, cardID):
        self.cardVendor = cardVendor
        self.cardID = cardID
        self.sum = 0.0

        self.lines = []

        with open(filename, "r", encoding="utf-8", errors="ignore") as f:
            self.lines = [line.replace("\x00", '').replace(",", "") for line in f.readlines()]

        self.num_of_lines = len(self.lines)

    def PrintSum(self, returnInstead = False):
        val = f"Card {self.cardID} from vendor {self.cardVendor}: {self.sum} "
        if returnInstead:
            return val
        print(val)

    def GetPartialSums(self):
        raise NotImplementedError()
    