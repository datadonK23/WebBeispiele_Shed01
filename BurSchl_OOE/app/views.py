"""
Views
"""

from flask import render_template, request, redirect, url_for
from app import app, connection, mapquest_key
from models import Features

# main page
@app.route("/")
def index(): 
    global features 
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
    
    # get and process features (Burgen)
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
    
    # get and process features (Schloesser)
    schloesser = features.get_schloesser()        
    schlossList = []
    for document in schloesser:
        feature = {}
        feature["name"] = document["name"].encode("utf-8")
        feature["url"] = document["url"].encode("utf-8")
        lng = round(document["loc"]["coordinates"][0], 7)
        lat = round(document["loc"]["coordinates"][1], 7)
        feature["coord"] = [lat, lng]
        schlossList.append(feature)
    
    # get and process features (Unklassifiziert)
    unclassifiedFeat = features.get_unbekannt()    
    unbList = []
    for document in unclassifiedFeat:
        feature = {}
        feature["name"] = document["name"].encode("utf-8")
        feature["url"] = document["url"].encode("utf-8")
        lng = round(document["loc"]["coordinates"][0], 7)
        lat = round(document["loc"]["coordinates"][1], 7)
        feature["coord"] = [lat, lng]
        unbList.append(feature)
    
    return render_template("index.html", MAPQUEST_KEY = map_key,
                           burgenList=burgenList, schlossList=schlossList,
                           unbList=unbList, stateBoundCoord=stateBoundCoord)


# Request location
@app.route("/loc/near/", methods= ["POST"])
def near():
    global coords
    
    # request coords
    lat = request.form["lat"]
    lng = request.form["lng"]
    coords = [round(float(lng), 7), round(float(lat), 7)]
    lng = "{:.7f}".format(coords[0])    
    lat = "{:.7f}".format(coords[1])
    coords = [lng, lat]
    
    return redirect(url_for("located", coords=str(coords)))
    

# Process location request and render nearest feature data                           
@app.route("/loc/<coords>/")
@app.route("/loc")
def located(coords=None):
    name = ""
    url = ""
    lat = 0.0
    lng = 0.0
    
    # get and process nearest feature from nearest feature list
    if coords:
        lng = float(coords[2:12])
        lat = float(coords[-12:-2])
        my_coords = [lng, lat]
        nearestFeat = features.get_nearest(my_coords)
        for document in nearestFeat:
            name = document["name"].encode("utf-8")
            url = document["url"].encode("utf-8")
            lng = round(document["loc"]["coordinates"][0], 7)
            lat = round(document["loc"]["coordinates"][1], 7)
    
    return render_template("located.html", n_name=name, n_url=url, n_lat=lat, 
                           n_lng=lng)


# Render information and references page
@app.route("/ref")
def ref():
    return render_template("ref.html")

