#conversion d'un fishier csv en fishier json
import json
import csv

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
    
    #ouvrir le fishier csv.
    with open('csvFilePath', encoding='utf-8') as csvf:
        readCSV = csv.DictReader(csvf)
        
        # conversion des ligne en dict python
        
        for rows in readCSV:
            jsonArray.append(rows)
      
            
    #conversion jsonarray en json
    with open('jsonFilePath', 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)
    
csvFilePath = 'C:/Users/Janvier/Documents/Lesson python/tp4/Annotation-export.csv'
jsonFilePath = 'C:/Users/Janvier/Documents/Lesson python/tp4/data.json'
csv_to_json(csvFilePath, jsonFilePath)
    