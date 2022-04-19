import argparse, datetime, json

from geopy.geocoders import Nominatim
"""

    Geolocation:
    - Perform the geoparsing on GPE and LOC entities. You can use Python
    GeoPy: https://geopy.readthedocs.io/en/stable/# or any other geoparsing tool you are familiar with. Be cognizant of the 
    potential API limits and make sure to optimize for the number of queries.
    - Make two dynamic maps that display the geolocated entities over time (day-by-day): a) The World map, where we can 
    observe the activities/mentions of the larger entities, such as countries; b) Ukraine map, to show the smaller entities that 
    appear in the news such as cities.
    You can use packages such as Plotly: https://plotly.com/python/maps/, or any other service you like (
    e.g. D3js: https://d3js.org/). A simple approach would be to take the snapshots of a map from each day and compile 
    them in a GIF. A more advanced approach would be to use tools such as mapbox that integrate with plotly. Here are some 
    ideas: -https://towardsdatascience.com/simple-plotly-tutorials-868bd0890b8b 
    -https://towardsdatascience.com/how-to-create-animated-scatter-maps-with-pl otly-and-dash-f10bb82d357a
    -https://plotly.com/python/maps/
    Any approach you choose will be considered valid.

    To install geopy I had to install using pip first and than conda:
        pip install geopy
        conda install -c conda-forge geopy
    
"""

def geoparse_data(array, name, date):
    for data in array:
        if not data[name]:
            continue
        print(data)
        geolocator = Nominatim(user_agent="dsci550-hw3")

        # get geolocation from address
        location = geolocator.geocode(data[name])
        
        if location:
            # print(location.address)
            # print((location.latitude, location.longitude))
            d = data[date].split("-")
            x = datetime.datetime(int(d[0]), int(d[1]), int(d[2]))
            v = location.address.split(",")
            print(v[len(v) - 1])
            # print(location.raw['address']['country_code'])
            print(x)
            # print(location.raw)            
        # else:
        #     print("No data found")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("--locs_file", dest="locs_file", help="A file containing the locs that will be geoparsed", required=True)
    parser.add_argument("--gpes_file", dest="gpes_file", help="A file containing the gpes that will be geoparsed", required=True)
    args = parser.parse_args()
    
    f = open(args.locs_file)
    data = json.load(f)    
    locs_array = data["locs"]
    locs_array_no_dupes = []
    [locs_array_no_dupes.append(x) for x in locs_array if x not in locs_array_no_dupes]
    
    
    f = open(args.gpes_file)
    data = json.load(f)    
    gpes_array = data["gpes"]
    gpes_array_no_dupes = []
    [gpes_array_no_dupes.append(x) for x in gpes_array if x not in gpes_array_no_dupes]
    
    # print(gpes_array)
    # print(gpes_array_no_dupes)
    # print(locs_array)
    # print(locs_array_no_dupes)
    
    geoparse_data(gpes_array, "name", "date")
    geoparse_data(locs_array, "name", "date")