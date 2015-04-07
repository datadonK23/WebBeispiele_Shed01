# -*- coding: utf-8 -*-
"""
Database Model

@author: Thomas Treml (datadonk23@gmail.com)
Date: 24.02.2015
"""

def get_db():
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.testDB
    return db

def add_track(db):
    db.tracks.insert({"name" : "A"})
    
def get_track(db):
    return db.tracks.find_one()

if __name__ == "__main__":

    db = get_db() 
    add_track(db)
    print get_track(db)

