import json
 
# Opening JSON file
f = open('working/inputs/json/311.full.json')
 
# returns JSON object as
# a dictionary
data = json.load(f)
 
# Iterating through the json
# list
print(data['summary'])
 
# Closing file
f.close()