import json, os, string

from country_lookup import get_country_location

subfolders = [ f.path for f in os.scandir("/Users/mikenicosia/Documents/School/USC/DSCI550/homework3") if f.is_dir() ]

subfolders.remove("/Users/mikenicosia/Documents/School/USC/DSCI550/homework3/dsci550-team")
subfolders.remove("/Users/mikenicosia/Documents/School/USC/DSCI550/homework3/map")

locations = {}

class Location:
    country: string
    latitude: float
    longitude: float

for subfolder in subfolders:
    print(subfolder)
    date_subfolders = [ f.path for f in os.scandir(subfolder) if f.is_dir() ]
    for date_subfolder in date_subfolders:
        arr = os.listdir(date_subfolder)
        for file_name in arr:
            if ".json" in file_name:
                f = open(date_subfolder + os.sep + file_name)
                ner_entries = json.load(f)
                date = "2022-3-" + file_name.split(".")[0].split("_")[1]
                print(date)
                for ner_entry in ner_entries:
                    if ner_entries[ner_entry] in ["LOC", "GPE"]:
                        ner_entry = ner_entry.replace("\n", " ").replace("The ", " ").replace("the ", " ").replace("'s", " ").strip().title()
                        if ner_entry in locations:
                            continue
                        location = get_country_location(ner_entry)
                        if not location is None:
                            l = {}
                            l["latitude"] = location.latitude
                            l["longitude"] = location.longitude
                            if "address" in location.raw and "country" in location.raw["address"]:
                                l["country"] = location.raw["address"]["country"]                                
                            locations[ner_entry] = l
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

with open('inputs/locations.json', 'w', encoding='utf8') as json_file:
    json.dump(locations, json_file, ensure_ascii=False)
    # json.dump(dict, file_pointer)