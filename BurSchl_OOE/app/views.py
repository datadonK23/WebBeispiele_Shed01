"""
Views
"""

from flask import render_template
from app import app
from app import connection
from app import mapquest_key
from models import Features

@app.route('/')
def index():
    map_key = mapquest_key
    # connect to model    
    features = Features(connection)
    # get state boundary     
    bounds = features.get_boundaries()   
    stateBoundCoord = []
    for bound in bounds:
        boundary = bound["loc"]["coordinates"][0]
        for coord in boundary:
            lon = round(coord[0], 7)
            lat = round(coord[1], 7)
            latlong = [lat, lon]
            stateBoundCoord.append(latlong)
    # get features (Burgen)
    burgen = features.get_burgen()        
    burgenList = []
    for document in burgen:
        feature = {}
        feature["name"] = document["name"].encode("utf-8")
        feature["url"] = document["url"].encode("utf-8")
        lng = round(document["loc"]["coordinates"][0], 7)
        lat = round(document["loc"]["coordinates"][1], 7)
        feature["coord"] = [lat, lng]
        burgenList.append(feature)
    return render_template('index.html', MAPQUEST_KEY = map_key,
                           burgenList=burgenList,
                           stateBoundCoord=stateBoundCoord)

@app.route('/ref')
def ref():
    return render_template('ref.html')

# test page
@app.route('/test')
def test():
    features = Features(connection)
    documents = features.get_burgen()
    namelist = []
    for document in documents:
        name = document["name"]
        namelist.append(name)
        
    burgen = features.get_burgen()
    featureList = []
    for document in burgen:
        feature = {}
        feature["name"] = document["name"].encode("utf-8")
        feature["url"] = document["url"].encode("utf-8")
        featureList.append(feature)
        lon = round(document["loc"]["coordinates"][0], 7)
        lat = round(document["loc"]["coordinates"][1], 7)
        feature["coord"] = [lat, lon]
    return render_template('ref.html', data=featureList)
