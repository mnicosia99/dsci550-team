import json, os, string

from country_lookup import get_country_location

"""
    This script performs preprocessing to create a list of locations for each LOC or GPE 
    found in the Named Entity Recognition processing.
"""
subfolders = [ f.path for f in os.scandir("/Users/mikenicosia/Documents/School/USC/DSCI550/homework3") if f.is_dir() ]

subfolders.remove("/Users/mikenicosia/Documents/School/USC/DSCI550/homework3/dsci550-team")
subfolders.remove("/Users/mikenicosia/Documents/School/USC/DSCI550/homework3/map")

locations = {}

class Location:
    country: string
    latitude: float
    longitude: float

for subfolder in subfolders:
    # For each news source and each date, parse the results of the NER
    # For each GPE and LOC, look up location data using the geopy library 
    # (wrapped in the country_lookup module).
    date_subfolders = [ f.path for f in os.scandir(subfolder) if f.is_dir() ]
    for date_subfolder in date_subfolders:
        arr = os.listdir(date_subfolder)
        for file_name in arr:
            if ".json" in file_name:
                f = open(date_subfolder + os.sep + file_name)
                ner_entries = json.load(f)
                date = "2022-3-" + file_name.split(".")[0].split("_")[1]
                for ner_entry in ner_entries:
                    if ner_entries[ner_entry] in ["LOC", "GPE"]:
                        #  some clean up of the data is needed to remove newlines, extra comma's, etc.
                        ner_entry = ner_entry.replace("\n", " ").replace("The ", " ").replace("the ", " ").replace("'s", " ").strip().title()
                        # go to the next if the data has already need queried
                        if ner_entry in locations:
                            continue
                        # get the location data
                        location = get_country_location(ner_entry)
                        if not location is None:
                            # if a location was found,  create a dictionary entry that will be 
                            # used to save as a json file
                            l = {}
                            l["latitude"] = location.latitude
                            l["longitude"] = location.longitude
                            # add countty if a country is found
                            if "address" in location.raw and "country" in location.raw["address"]:
                                l["country"] = location.raw["address"]["country"]                                
                            locations[ner_entry] = l
                            # always add lat/long
                            if "address" in location.raw and "country" in location.raw["address"]:
                                if location.raw["address"]["country"] in locations:
                                    continue
                                location = get_country_location(location.raw["address"]["country"])
                                if not location is None:
                                    l = {}
                                    l["latitude"] = location.latitude
                                    l["longitude"] = location.longitude
                                    if "address" in location.raw and "country" in location.raw["address"]:
                                        l["country"] = location.raw["address"]["country"]                                
                                    locations[location.raw["address"]["country"]] = l
                        else:
                            print("Unable to find location for " + ner_entry)
                            
# f = open("tests/locations.json")
# data = json.load(f)          
# json_string = json.dumps(data, ensure_ascii=False).encode('utf8')
# print(json_string.decode())

# save the dictionary as a json file for use later
with open('inputs/locations.json', 'w', encoding='utf8') as json_file:
    json.dump(locations, json_file, ensure_ascii=False)
    # json.dump(dict, file_pointer)