import json, os

from Mentions import Mention, MentionType
from country_lookup import get_mapping
from map_plot import display_on_map

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

fw = open("output/collected_data_ukraine.csv", "w")
date_map = {}

# Load the preprocessed locations
loc_file = open("input/locations.json")
locations = json.load(loc_file)          

# for each NER/LOC look up the location and keep a sum per day for each city in Ukraine
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
                    if ner_entries[ner_entry] in ["LOC", "GPE"]:
                        ner_entry = ner_entry.replace("\n", " ").replace("The ", " ").replace("the ", " ").replace("'s", " ").strip().title()
                        ner_entry = get_mapping(ner_entry)
                        ukraine_data = {}
                        if date in date_map:
                            ukraine_data = date_map[date]
                            del date_map[date]
                        inc = 0
                        if not ner_entry in locations:
                            continue
                        location = locations[ner_entry]
                        # For all locations in Ukraine, sum up all times the city was mentioned each day
                        if not location is None:
                            if "country" in location:
                                if "Ukraine" == location["country"] or "Україна" in location["country"]:
                                    mention:Mention = add_mention(location["country"], ner_entry, date, location["latitude"], location["longitude"], MentionType.PRIMARY)
                                    if ner_entry in ukraine_data:
                                        inc = ukraine_data[ner_entry].count
                                        del ukraine_data[ner_entry]
                                    mention.count = inc + 1
                                    ukraine_data[ner_entry] = mention
                        date_map[date] = ukraine_data
                            
# Write the csv file for each country for each day
fw.write("Country,Date,Label,Latitude,Longitude,Count,Type\n")
for date in date_map:
    for country in date_map[date]:
        fw.write(date_map[date][country].as_csv() + "\n")
fw.close()

# Display the csv data on the map
display_on_map(os.path.realpath(fw.name))