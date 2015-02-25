# -*- coding: utf-8 -*-
"""
Database Model

@author: Thomas Treml (datadonk23@gmail.com)
Date: 25.02.2015
"""

import json
from pymongo import MongoClient

def get_db():
    """ 
    db object
    """
    cli = MongoClient('localhost:27017')
    db = cli.FeBSOOE
    return db

def insert_db(db):
    """
    set up db entries
    """
    # load geojson file
    with open('febs.geojson') as f:
    data = json.load(f)
    
    # process data
    for feature in data['features']:
        print (str(feature["properties"]["name"]) + " : " + 
        str(feature['geometry']['coordinates']))
    # insert in db

def get_castle(db):
    """ test fu """
    return db.FeBS.find_one()


