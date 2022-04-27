import random

from iso3166 import countries
from geopy.geocoders import Nominatim

"""
    This script privides some utilities relation to locations.
"""

# This map was created to address differences in how the same country was 
# listed in the output of the NER.
country_map = {}
country_map["United States"] = "United States of America"
country_map["England"] = "United Kingdom"
country_map["Russia"] = "Russian Federation"

# This map was created to address typos as well as different spellings for cities.
# Different spellings are primarily for Ukrainian towns and villages that could not 
# be looked up in the geopy library.
mapping = {}
mapping["Zhytomir"] = "Zhytomyr"
mapping["Zaporiznznia"] = "Zaporizhzhia"
mapping["Krasnopillya"] = "Sumy"
mapping["Nemishajeve"] = "Kyiv"
mapping["Zaporizhzia"] = "Zaporizhzhia"
mapping["Lviv  Ekaterina Kryshtal"] = "Lviv"
mapping["Lviv  Residents"] = "Lviv"
mapping["Lviv  Russian"] = "Lviv"
mapping["Chemihiv"] = "Chernihiv"
mapping["Mykolalv"] = "Mykolaiv"
mapping["Bediansk"] = "Mariupol"
mapping["Nova Lyubomyrka"] = "Rivne"
mapping["Popasana"] = "Popasna"
mapping["Transnitsia"] = "Transnistria"
mapping["Novooleksiika"] = "Crimean Peninsula"
mapping["Zelenogai"] = "Crimean Peninsula"
mapping["Okhmatdyt"] = "Kyiv"
mapping["Enerdohar"] = "Zaporizhzhia"
mapping["Ukrainevaccording\To"] = "Ukraine"
mapping["Berestyanka"] = "Kyiv"
mapping["Novopskoy"] = "Novopskov"
mapping["Nemeshaevo"] = "Mykulychi"
mapping["Chuhuiy"] = "Chuhuiv"
mapping["Kyslytsya"] = "Odessa Oblast"
mapping["Lviv  Russia"] = "Lviv"
mapping["Transdniestria"] = "Transnistria"
mapping["Chenihiv"] = "Chernihiv"
mapping["Luhuansk"] = "Luhansk"
mapping["Zmiiny"] = "Zmiinyi Island"
mapping["Mykolaiy"] = "Mykolaiv"
mapping["Sivershchyna"] = "Chernihiv"
mapping["Kuvshynova"] = "Oleksandra"
mapping["Oleksandra Kuvshynova"] = "Oleksandra"
mapping["Chemihiy"] = "Chernihiv"
mapping["Chemniiv"] = "Chernihiv"
mapping["Chemnihiv"] = "Chernihiv"
mapping["Cherniniy"] = "Chernihiv"
mapping["Northern Ukraine"] = "Chernihiv"
mapping["Damytskyi"] = "Kyiv"
mapping["Chemobyl"] = "Chernobyl"
mapping["Chernolbyl"] = "Chernobyl"
mapping["Vasykkv"] = "Kyiv"
mapping["Vasikyiv"] = "Kyiv"
mapping["Kharkiin"] = "Kharkiv"
mapping["Brusyn"] = "Donetsk Oblast"
mapping["Ukrainian"] = "Ukraine"
mapping["Kostyantynivka"] = "Donetsk Oblast"

# returns city mappings
def get_mapping(entry):
    if entry in mapping:
        return mapping[entry]
    else:
        return entry

# Checks if a value is the name of a country
def is_country(value):  
    if value in country_map:
        value = country_map[value]
    f = False  

    for cl in countries:
        if value == cl.name:
            f = True
            break
        elif value in cl.name:
            f = True

    return f

# Use geopy library to look up a location for a given name   
def get_country_location(name):  
    nbr = random.randint(0, 999)
    geolocator = Nominatim(user_agent="dsci550-hw3-" + str(nbr), timeout=None)
    location = geolocator.geocode(name, namedetails=True, addressdetails=True)
    return location
    