class CardFileExtractor:
    def __init__(self, filename, cardVendor, cardID):
        self.cardVendor = cardVendor
        self.cardID = cardID

        self.lines = []

        with open(filename, "r", encoding="utf-8", errors="ignore") as f:
            self.lines = [line.replace("\x00", '').replace(",", "") for line in f.readlines()]

        self.num_of_lines = len(self.lines)
        