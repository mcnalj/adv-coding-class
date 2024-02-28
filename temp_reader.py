import csv

with open('moody.csv') as moody:
    reader = csv.reader(moody)
    next(reader)
    minimum = 2000
    for blah in reader:
        if int(blah[1]) < minimum:
            minimum = int(blah[1])
    print(minimum)
        

