# -*- coding: utf-8 -*-
"""
Database Model

@author: Thomas Treml (datadonk23@gmail.com)
Date: 26.02.2015
"""

import json
from pymongo import MongoClient
from pymongo import collection


def get_db():
    """ 
    db object
    """
    cli = MongoClient("localhost:27017")
    db = cli.FeBSOOE
    return db

def set_collection(db, collection_name):
    db.create_collection(collection_name)
    
def get_collection(db, collection_name):
    return collection.Collection(db, collection_name)
    
def create_index(collection):
    from pymongo import GEOSPHERE as GEOIX
    collection.create_index([("loc", GEOIX)])

"2dsphere" 
def insert_db(collection):
    """
    process feature and insert to db
    """
    # load geojson file
    with open("febs.geojson") as f:
        data = json.load(f)
    
    # process data
    for feature in data["features"]:
        feature_dict = {}
        location = {}
        feature_type = (feature["geometry"]["type"]).encode()
        feature_dict["name"] = (feature["properties"]["name"]).encode()
        location["type"] = feature_type
        location["coordinates"] = feature["geometry"]["coordinates"] 
        feature_dict["loc"] = location
        
        #FIXME URL        
        
        # insert in db collection        
        collection.insert(feature_dict)

def get_castle(db):
    """ test fu """
    return db.febs.find_one({"name": "Cumberland"})

db = get_db()
#set_collection(db, "febs")
coll = get_collection(db, "febs")
#insert_db(coll)
#create_index(coll)



