import json, os, string
from datetime import datetime
from enum import Enum

import pycountry
from geopy.geocoders import Nominatim
    
class MentionType(Enum):
    PRIMARY = "primary"
    SECONDARY = "secondary"
    
class Mention:
    date: datetime
    type: string
    country: string
    label: string
    latitude: float
    longitude: float
    count: int

    def __str__(self):
        return "Label: " +  self.label + " Type: " +  str(self.type) + " Date: " +  self.date + " Count: " + str(self.count)  
    
    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Mention):
            return self.label == other.label and self.type == other.type and self.date == other.date
        return False
        
    def __hash__(self):
        return hash(self.label + self.date + str(self.type))
    
    def as_csv(self):
        return self.country + "," + self.date + "," + self.label + "," + str(self.latitude) + "," + str(self.longitude) + "," + str(self.count) + "," + self.type

def add_mention(country, label, date, lat, lon, type):
    mention = Mention()
    mention.count = 0
    mention.country = country
    mention.date = date
    mention.label = label
    mention.latitude = lat
    mention.longitude = lon
    mention.type = str(type)
    return mention
    
subfolders = [ f.path for f in os.scandir("/Users/mikenicosia/Documents/School/USC/DSCI550/homework3") if f.is_dir() ]

subfolders.remove("/Users/mikenicosia/Documents/School/USC/DSCI550/homework3/dsci550-team")
subfolders.remove("/Users/mikenicosia/Documents/School/USC/DSCI550/homework3/map")

mentions_map = {}
ukraine_mentions = {}

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
                    if ner_entries[ner_entry] in ["LOC", "GPE"]:
                        geolocator = Nominatim(user_agent="dsci550-hw3-" + str(count), timeout=None)
                        count += 1

                        # get geolocation from address
                        location = geolocator.geocode(ner_entry)
                        if location:
                            if "Ukraine" in location.address or "Україна" in location.address:
                                mention:Mention = add_mention("Ukraine", str(location.address), date, location.latitude, location.longitude, MentionType.SECONDARY)
                                ukraine_mentions[mention] = mention
                                jsonStr = json.dumps(mention.__dict__, indent=4, ensure_ascii=False).encode('utf8')
                            for c in pycountry.countries:
                                # Is it a primary or secondary reference
                                if c.name in ner_entry:
                                    inc = 0
                                    mention:Mention = add_mention(c.name, c.name, date, location.latitude, location.longitude, MentionType.PRIMARY)
                                    if mention in mentions_map:
                                        inc = mentions_map[mention]
                                        del mentions_map[mention]
                                    mention.count = inc + 1
                                    mentions_map[mention] = mention.count
                                if c.name in location.address:
                                    inc = 0
                                    mention:Mention = add_mention(c.name, c.name, date, location.latitude, location.longitude, MentionType.SECONDARY)
                                    if mention in mentions_map:
                                        inc = mentions_map[mention]
                                        del mentions_map[mention]
                                    mention.count = inc + 1
                                    mentions_map[mention] = mention.count
                                    break
ukraine_mentions_file = open("ukraine_result.csv", "w")
ukraine_mentions_file.write("Country,Date,Label,Latitude,Longitude,Count,Type\n")
country_mentions_file = open("countries_result.csv", "w")
country_mentions_file.write("Country,Date,Label,Latitude,Longitude,Count,Type\n")
for mention in mentions_map:
    country_mentions_file.write(mention.as_csv() + "\n")
    # jsonStr = json.dumps(mention.__dict__, indent=4)
    # print(jsonStr)
for mention in ukraine_mentions:
    ukraine_mentions_file.write(mention.as_csv() + "\n")
    # jsonStr = json.dumps(mention.__dict__, indent=4)
    # print(jsonStr)
