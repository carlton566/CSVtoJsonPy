import csv
import json
with open('pick2.csv',encoding="utf-8-sig") as f:
    reader = csv.reader(f, skipinitialspace=True)
    header = next(reader)
    a = [dict(zip(header, map(str, row))) for row in reader]

file1 = open('pick2.txt', 'w')
file1.write(json.dumps(a))
file1.close()