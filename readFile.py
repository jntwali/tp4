#lire un fishier csv
import csv
import json
import io
with open("C:/Users/Janvier/Documents/Lesson python/tp4/Annotation-export.csv","r+",newline='') as csvfile:
    
    newFile = csv.reader(csvfile, delimiter=',')
    for index in newFile:
        print(json.dump(index,fp = io))
#for line in newFile:
    #print(line)
#newFile.readlines()
#for index in range(10):
  #  line = next(newFile)
  #  print(line)
#newFile.close()
#import io



#for index in range(5):
#    raw=next(newFile)
#    print(raw)