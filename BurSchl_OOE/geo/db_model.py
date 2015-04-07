# -*- coding: utf-8 -*-
"""
Database Model
Purpose: Set up MongoDB and insert data from GeoJSON file
@author: Thomas Treml (datadonk23@gmail.com)
Date: 03.03.2015
"""

import json
from pymongo import MongoClient
from pymongo import collection


def get_db():
    """ 
    db object
    """
    cli = MongoClient("localhost:27017")
    db = cli.BSOOE
    return db

def set_collection(db, collection_name):
    db.create_collection(collection_name)
    
def get_collection(db, collection_name):
    return collection.Collection(db, collection_name)
    
def create_index(collection):
    """ 2d sphere Index """ 
    from pymongo import GEOSPHERE as GEOIX
    collection.create_index([("loc", GEOIX)])

def insert_point(collection):
    """
    Shuffle point data from GeoJSON to DB Document and insert into DB 
    """
    # load geojson file
    with open("../data/febs_wiki.geojson") as f:
        data = json.load(f)
    
    # geojson to mongo doc
    for feature in data["features"]:
        feature_dict = {}
        feature_dict["name"] = feature["properties"]["name"]
        feature_dict["type"] = feature["properties"]["type"]
        feature_dict["url"] = feature["properties"]["url"]
        location = {}
        feature_type = feature["geometry"]["type"]
        location["type"] = feature_type
        location["coordinates"] = feature["geometry"]["coordinates"] 
        feature_dict["loc"] = location
        
        # insert in db collection        
        collection.insert(feature_dict)

def insert_poly(collection):
    """
    Shuffle polygon data from GeoJSON to DB Document and insert into DB 
    """
    # load geojson file
    with open("../data/landesgrenze_WGS84.geojson") as f:
        data = json.load(f)
    
    # geojson to mongo doc
    for feature in data["features"]:
        feature_dict = {}
        feature_dict["name"] = "state_boundary"
        feature_dict["loc"] = feature["geometry"]
        
        # insert in db collection        
        collection.insert(feature_dict)

def get_testdata(db):
    """ test fu """
    feat = [db.febs.find_one({"name": "Schloss Wolfsegg"})]
    feat.append(db.bound.find_one())
    return feat

db = get_db()
set_collection(db, "febs")
set_collection(db, "bound")
coll = get_collection(db, "febs")
insert_point(coll)
create_index(coll)
coll = get_collection(db, "bound")
insert_poly(coll)
create_index(coll)

print "...done"
