#!/usr/bin/env python

from faker import Faker
import json, os, random
from datetime import timedelta
from datetime import datetime

SCRIPT_PATH = os.path.realpath(__file__).replace("/fakedata.py", "")
"""
    This script provides various methods to fake data including names and dates
    and also provides methods to retiurn random university names and majors from an existing list.
    
    Dependencies: faker

"""
def get_number_authors():
    return random.randint(1, 5)

def get_date(start_days_ago=1, end_days_ago=365):
        days_ago = random.randint(start_days_ago, end_days_ago)
        pub_datetime = datetime.now() - timedelta(days=days_ago)

        publish_date = pub_datetime.strftime('%m-%d-%Y')
        iso_date = pub_datetime.isoformat()
        
        print(publish_date)
        print(iso_date)
        return publish_date

def create_authors(nbr_authors=get_number_authors()):
    authors = list()
    
    for i in range(nbr_authors):
        faker = Faker()
        authors.append(faker.name())            
    return authors

def get_random_school():
    f = open(SCRIPT_PATH + os.sep + "inputs" + os.sep + "universities.json")
    universities = json.load(f)
    inx = random.randint(0, len(universities) - 1)
    return universities[inx]["institution"]
        
def get_random_department():
    mf = open(SCRIPT_PATH + os.sep + "inputs" + os.sep + "majors.json")
    majors = json.load(mf)
    inx = random.randint(0, len(majors["majors"]) - 1)
    return "School of " + majors["majors"][inx]["department"]
