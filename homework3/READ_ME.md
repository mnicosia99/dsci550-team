# Homework 3 Folder

Contains files needed for homework 3.

#### OCR, saving extracted text, named entity recognition and analysis (NER)
Link contains all the folders for the images, texts extracted, and tokenization from texts.
https://drive.google.com/drive/folders/1Na-wf7FhTfL_ecuyuyPh5QYxsnxMCqKI?usp=sharing

Folders:
    
    Final Images after OCR using Tesseract per day of month:
    Longcat_2000px_images 
    map_plotting - Contains the code that pasred the NER results for LOC and GPE references and looked up 
                   geolocation data and plotted on map including the number of times a reference was made 
                   per day.
    
    Text Extraction for three news sources into .txt formats per day of month:
    aljazeera_text
    cnn_text
    fox_text
    
    Tokenization and performing NER with SpaCY on three news sources:
    aljazeera_NER_tokenization
    cnn_NER_tokenization
    fox_NER_tokenization

Code to run split Images:
python test_longcat.py
    
    Requirements: python libraries
        __future__, PIL, math,os

Code to extract text: 
python extract_text.py
     
     Requirements: python libraries
           PIL, pytesseract, os

Code to tokenize text:
python token_text.py
    
    Requirements: python libraries
        spacy, os, json

Note: Please update the input and output directories in each .py file according to where the input files are located and where you want output file saved

#### Plot Distributions from NER 

#### Geolocation

Code to geoparse LOC and GPE in a preprocess stage:
    
    map_plotting/get_location_data.py

    Requirements: json, os, string

    Output:  Creates a locations json file in the map_plotting/input directory

Code to process location data and sum counts per day for countries:
    
    map_plotting/collect_data_countries.py

    Requirements: json, os

    Inputs:  A locations json file in the map_plotting/input directory

    Output:  Creates a countries csv file in the map_plotting/output directory

Code to process location data and sum counts per day for Ukrainian cities:
    
    map_plotting/collect_data_ukraine.py

    Requirements: json, os

    Inputs:  A locations json file in the map_plotting/input directory

    Output:  Creates a ukraine csv file in the map_plotting/output directory

Location utilities used for location lookups and identification if a NER key is a country:
    
    map_plotting/country_lookup.py

    Requirements: random, iso3166, geopy

Mapping utility to display geolocated data on a map using plotly:
    
    map_plotting/map_plot.py

    Requirements: plotly, pandas

    Inputs:  A csv json file in the map_plotting/output directory containing lat/long, date, country and label data.

Script to sum up references per date and new source:
    
    map_plotting/loc_gpe_counts.py

    Requirements: json, os, string, datetime

    Inputs:  A locations json file in the map_plotting/input directory

    Output:  Creates two csv files containing the GPE and LOC data respectively.
