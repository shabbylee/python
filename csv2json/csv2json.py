import json
import csv
with open('test_data.csv', 'r') as f:
    # for i in range(4):
    #     f.readline()
    fcsv = csv.DictReader(f)
    print type(fcsv)
    for x in fcsv:
        print x
        print json.dumps(x)
    y = json.dumps(x)
    print type(y)
    print y[0]
    print type(x)
    print x['body']
    print len(x)

import csv
import json

csvfile = open('test_data.csv', 'r')
jsonfile = open('test_data.json', 'w')

fieldnames = ("URL","method","header","body")
reader = csv.DictReader(csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')