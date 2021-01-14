from FileExtractors.CALFileExtractor import CALFileExtractor

card = CALFileExtractor(filename = "Transactions_02_01_2021.xls", cardID = "5928")
print(card.PrintSum(True))