import json, os, string
from datetime import datetime
from enum import Enum

from country_lookup import get_mapping

class MentionType(Enum):
    PRIMARY = "primary"
    SECONDARY = "secondary"
    
class Mention:
    date: datetime
    source: string
    id: string
    label: string
    latitude: float
    longitude: float
    count: int

    def __str__(self):
        return "Label: " +  self.label + " Source: " +  self.source + " Date: " +  self.date + " Count: " + str(self.count)  
    
    def __eq__(self, other):
        if isinstance(other, Mention):
            return self.label == other.label and self.date == other.date and self.source == other.source
        return False
        
    def __hash__(self):
        return hash(self.label + self.date + self.source)
    
    def as_csv(self):
        return self.id + "," + self.date + "," + self.label + "," + str(self.latitude) + "," + str(self.longitude) + "," + str(self.count) + "," + self.source

def create_mention(id, label, date, lat, lon, source):
    mention = Mention()
    mention.count = 0
    mention.id = id
    mention.date = date
    mention.label = label
    mention.latitude = lat
    mention.longitude = lon
    mention.source = source
    return mention
    
subfolders = [ f.path for f in os.scandir("/Users/mikenicosia/Documents/School/USC/DSCI550/homework3") if f.is_dir() ]

subfolders.remove("/Users/mikenicosia/Documents/School/USC/DSCI550/homework3/dsci550-team")
subfolders.remove("/Users/mikenicosia/Documents/School/USC/DSCI550/homework3/map")

mentions_map_loc = {}
mentions_map_gpe = {}

# Load the preprocessed locations
loc_file = open("input/locations.json")
locations = json.load(loc_file)          

# for each NER/LOC look up the location and keep a sum per day for each key and source
for subfolder in subfolders:
    date_subfolders = [ f.path for f in os.scandir(subfolder) if f.is_dir() ]
    for date_subfolder in date_subfolders:
        arr = os.listdir(date_subfolder)
        for file_name in arr:
            if ".json" in file_name:
                f = open(date_subfolder + os.sep + file_name)
                ner_entries = json.load(f)
                date = "2022-3-" + file_name.split(".")[0].split("_")[1]
                for ner_entry in ner_entries:
                    # For all locations, sum up all times a reference was made for each day and osurce
                    if ner_entries[ner_entry] == "GPE":
                        ner_entry = ner_entry.replace("\n", " ").replace("The ", " ").replace("the ", " ").replace("'s", " ").strip().title()
                        ner_entry = get_mapping(ner_entry)
                        location = None
                        if ner_entry in locations:
                            location = locations[ner_entry]

                        if location is None or not "address" in location:
                            # add without address, using ner_entry as the key   
                            inc = 0
                            mention:Mention = create_mention(ner_entry, ner_entry, date, None, None, subfolder.replace("_NER_tokenization", "").replace("/Users/mikenicosia/Documents/School/USC/DSCI550/homework3/", ""))
                            if ner_entry in mentions_map_gpe:
                                mention = mentions_map_gpe[ner_entry]
                                inc = mention.count
                                del mentions_map_gpe[ner_entry]
                            mention.count = inc + 1
                            mentions_map_gpe[ner_entry] = mention                            
                        else:                     
                            address = location.address                        
                            inc = 0
                            mention:Mention = create_mention(ner_entry, location.address, date, location.latitude, location.longitude, subfolder.replace("_NER_tokenization", "").replace("/Users/mikenicosia/Documents/School/USC/DSCI550/homework3/", ""))
                            if address in mentions_map_gpe:
                                mention = mentions_map_gpe[address]
                                inc = mention.count
                                del mentions_map_gpe[address]
                            mention.count = inc + 1
                            mentions_map_gpe[address] = mention                            
                    elif ner_entries[ner_entry]  == "LOC":
                        ner_entry = ner_entry.replace("\n", " ").replace("The ", " ").replace("the ", " ").replace("'s", " ").strip().title()
                        ner_entry = get_mapping(ner_entry)
                        location = None
                        if ner_entry in locations:
                            location = locations[ner_entry]

                        if location is None or not "address" in location:
                            # add without address, using ner_entry as the key   
                            inc = 0
                            mention:Mention = create_mention(ner_entry, ner_entry, date, None, None, subfolder.replace("_NER_tokenization", "").replace("/Users/mikenicosia/Documents/School/USC/DSCI550/homework3/", ""))
                            if ner_entry in mentions_map_loc:
                                mention = mentions_map_loc[ner_entry]
                                inc = mention.count
                                del mentions_map_loc[ner_entry]
                            mention.count = inc + 1
                            mentions_map_loc[ner_entry] = mention                            
                        else:                     
                            address = location.address                        
                            inc = 0
                            mention:Mention = create_mention(ner_entry, location.address, date, location.latitude, location.longitude, subfolder.replace("_NER_tokenization", "").replace("/Users/mikenicosia/Documents/School/USC/DSCI550/homework3/", ""))
                            if address in mentions_map_loc:
                                mention = mentions_map_loc[address]
                                inc = mention.count
                                del mentions_map_loc[address]
                            mention.count = inc + 1
                            mentions_map_loc[address] = mention                            

# Write the csv file for each country for each day
loc_mentions_file = open("output/loc_counts.csv", "w")
loc_mentions_file.write("ID,Date,Label,Latitude,Longitude,Count,Source\n")
for key in mentions_map_loc:
    loc_mentions_file.write(mentions_map_loc[key].as_csv() + "\n")

gpe_mentions_file = open("output/gpe_counts.csv", "w")
gpe_mentions_file.write("ID,Date,Label,Latitude,Longitude,Count,Source\n")
for key in mentions_map_gpe:
    gpe_mentions_file.write(mentions_map_gpe[key].as_csv() + "\n")
