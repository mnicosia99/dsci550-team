import json, os, re, string
from datetime import datetime
from enum import Enum

from geopy.geocoders import Nominatim
    
class MentionType(Enum):
    PRIMARY = "primary"
    SECONDARY = "secondary"
    
class Mention:
    date: datetime
    type: string
    id: string
    label: string
    latitude: float
    longitude: float
    count: int

    def __str__(self):
        return "Label: " +  self.label + " Type: " +  str(self.type) + " Date: " +  self.date + " Count: " + str(self.count)  
    
    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Mention):
            return self.label == other.label and self.date == other.date
        return False
        
    def __hash__(self):
        return hash(self.label + self.date)
    
    def as_csv(self):
        return self.id + "," + self.date + "," + self.label + "," + str(self.latitude) + "," + str(self.longitude) + "," + str(self.count) + "," + self.type

def create_mention(id, label, date, lat, lon, type):
    mention = Mention()
    mention.count = 0
    mention.id = id
    mention.date = date
    mention.label = label
    mention.latitude = lat
    mention.longitude = lon
    mention.type = str(type)
    return mention
    
subfolders = [ f.path for f in os.scandir("/Users/mikenicosia/Documents/School/USC/DSCI550/homework3") if f.is_dir() ]

subfolders.remove("/Users/mikenicosia/Documents/School/USC/DSCI550/homework3/dsci550-team")
subfolders.remove("/Users/mikenicosia/Documents/School/USC/DSCI550/homework3/map")

mentions_map_loc = {}
mentions_map_gpe = {}

for subfolder in subfolders:
    print(subfolder)
    count = 0
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
                    if ner_entries[ner_entry] == "GPE":
                        ner_entry = ner_entry.replace("\n", " ").replace("\"", "\'").replace(",", " ")
                        geolocator = Nominatim(user_agent="dsci550-hw3-" + str(count), timeout=None)
                        count += 1
                        # get geolocation from address
                        ner_entry = re.sub('the ','', ner_entry)
                        ner_entry = re.sub('\'s','', ner_entry)
                        location = geolocator.geocode(ner_entry, namedetails=True, addressdetails=True)
                        if location is None:
                            print("Could not find address for " + ner_entry)
                            # add without address, using ner_entry as the key   
                            inc = 0
                            mention:Mention = create_mention(ner_entry, ner_entry, date, None, None, MentionType.PRIMARY)
                            if ner_entry in mentions_map_gpe:
                                print("Already found " + ner_entry + " for " + ner_entry + " as " + mentions_map_gpe[ner_entry].id)
                                mention = mentions_map_gpe[ner_entry]
                                inc = mention.count
                                del mentions_map_gpe[ner_entry]
                            mention.count = inc + 1
                            mentions_map_gpe[ner_entry] = mention                            
                        else:                     
                            address = location.address                        
                            inc = 0
                            mention:Mention = create_mention(ner_entry, location.address, date, location.latitude, location.longitude, MentionType.PRIMARY)
                            if address in mentions_map_gpe:
                                print("Already found " + location.address + " for " + ner_entry + " as " + mentions_map_gpe[address].id)
                                mention = mentions_map_gpe[address]
                                inc = mention.count
                                del mentions_map_gpe[address]
                            mention.count = inc + 1
                            mentions_map_gpe[address] = mention                            
                    elif ner_entries[ner_entry]  == "LOC":
                        ner_entry = ner_entry.replace("\n", " ").replace("\"", "\'").replace(",", " ")
                        geolocator = Nominatim(user_agent="dsci550-hw3-" + str(count), timeout=None)
                        count += 1
                        # get geolocation from address
                        ner_entry = re.sub('the ','', ner_entry)
                        ner_entry = re.sub('\'s','', ner_entry)
                        location = geolocator.geocode(ner_entry, namedetails=True, addressdetails=True)
                        if location is None:
                            print("Could not find address for " + ner_entry)
                            # add without address, using ner_entry as the key   
                            inc = 0
                            mention:Mention = create_mention(ner_entry, ner_entry, date, None, None, MentionType.PRIMARY)
                            if ner_entry in mentions_map_loc:
                                print("Already found " + ner_entry + " for " + ner_entry + " as " + mentions_map_loc[ner_entry].id)
                                mention = mentions_map_loc[ner_entry]
                                inc = mention.count
                                del mentions_map_loc[ner_entry]
                            mention.count = inc + 1
                            mentions_map_loc[ner_entry] = mention                            
                        else:                     
                            address = location.address                        
                            inc = 0
                            mention:Mention = create_mention(ner_entry, location.address, date, location.latitude, location.longitude, MentionType.PRIMARY)
                            if address in mentions_map_loc:
                                print("Already found " + location.address + " for " + ner_entry + " as " + mentions_map_loc[address].id)
                                mention = mentions_map_loc[address]
                                inc = mention.count
                                del mentions_map_loc[address]
                            mention.count = inc + 1
                            mentions_map_loc[address] = mention                            

loc_mentions_file = open("output/loc_locs_gpes.csv", "w")
loc_mentions_file.write("ID,Date,Label,Latitude,Longitude,Count,Type\n")
for key in mentions_map_loc:
    loc_mentions_file.write(mentions_map_loc[key].as_csv() + "\n")

gpe_mentions_file = open("output/gpe_locs_gpes.csv", "w")
gpe_mentions_file.write("ID,Date,Label,Latitude,Longitude,Count,Type\n")
for key in mentions_map_gpe:
    gpe_mentions_file.write(mentions_map_gpe[key].as_csv() + "\n")
