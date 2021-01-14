lines = []
fileName = "Transactions_02_01_2021.xls"
with open(fileName, "r", encoding="utf-8", errors="ignore") as f:
    lines = [line.replace("\x00", '').replace(",", "").split('\t') for line in f.readlines()]

    print(f'{len(lines)} lines extracted from "{fileName}" ')

count = 0
sum = 0.0
for line in lines:
    count += 1
    if count <= 3 or count == len(lines):
        continue

    colVal = (line[0], float(line[3].rstrip()))

    print(colVal)
    sum += colVal[1]

print(f'Total: {sum}')
