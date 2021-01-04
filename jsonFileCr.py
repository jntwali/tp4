#create json file
import csv
import json

csvfile = open('C:/Users/Janvier/Documents/Lesson python/tp4/Annotation-export.csv','r')
jsonfile = open('file.json','w')

fieldnames = ('Image','xmin','ymin','xmax','ymax','label')
reader = csv.DictReader(csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')
