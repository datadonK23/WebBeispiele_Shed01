# -*- coding: utf-8 -*-
"""
Scrape Wikipedia List of Castles in Upper AUT
Purpose: Scrape list of castles in Upper Austria from German Wikipedia and get 
         Name, Geo-Coordinates, Wikipedia-URL and classify Type
@author: Thomas Treml (datadonk23@gmail.com)
Date: 02.03.2015
"""

import wikipedia
from bs4 import BeautifulSoup
from json import dumps
from decimal import Decimal

febs = []
urls = []
error_names = []

# Deutsche Wikipedia Version
wikipedia.set_lang("de")

# Vorprozessierte Datei mit Links aus Wiki Liste
with open("wiki_links.html") as f:
    soup = BeautifulSoup(f)

# Suche Links
links=soup.find_all("a")
for i in range(len(links)):
    # Überspringe jeden zweiten Link    
    if i % 2 == 0:
        url = links[i].get("href")
        urls.append(url)

def fetch_features(page_pointer):
    """
    Features von Wiki Page extrahieren. Features: Name, (geo) Koordinaten, 
    Type (Burg / Schloss / unb(ekannt)).
    Gibt Dict mit Features als Key und jeweilige Werte zurück
    """
    features = {}
    features["name"] = page_pointer.title
    try:
        features["loc"] = page_pointer.coordinates
    except:
        features["loc"] = ["0", "0"]
    try:
        features["url"] = page_pointer.url
    except:
        features["url"] = ""
    if "urg" in features["name"]: # REGEX
        features["type"] = "Burg"
    elif "chlo" in features["name"]:
        features["type"] = "Schloss"
    else:
        features["type"] = "unb"
    return features

# Parse durch Links und logge Fehler
for i in range(len(urls)):
    print "processing #" + str(i) + " from " + str(len(urls)-1)
    try:
        page_pointer = wikipedia.page(urls[i][6:])
        features = fetch_features(page_pointer)
        febs.append(features)
    except wikipedia.exceptions.PageError:
        try: # Klammern Umgang
            page_pointer = wikipedia.page((urls[i][6:]).replace("(",
                                          "").replace(")", ""))
            features = fetch_features(page_pointer)
            febs.append(features)           
        except:
            try: # Sonderzeichen und Abkuerzungen Umgang 
                page_pointer = wikipedia.page((urls[i][6:]).replace("%C3%B6", 
                "ö").replace("%C3%96", "Ö").replace("%C3%BC", "ü").replace(
                "%C3%9F", "ss").replace("%C3%A4", "ä").replace("St.", 
                "Sankt").replace("-", "_").replace("(", "").replace(")", ""))
                features = fetch_features(page_pointer)
                febs.append(features)
            except:
                try: # Sonderzeichen + besondere Abk. Umgang
                    page_pointer = wikipedia.page((urls[i][6:]).replace(
                    "%C3%B6", "ö").replace("%C3%96", "Ö").replace("%C3%BC", 
                    "ü").replace("%C3%9F", "ss").replace("%C3%A4", 
                    "ä").replace("St.", "st").replace("-", "_").replace("(", 
                    "").replace(")", ""))
                    features = fetch_features(page_pointer)
                    febs.append(features)
                except:
                    error_name = urls[i][6:]
                    error_names.append(error_name)
    i+=1

# Schreibe GeoJSON
print "Schreibe GeoJSON"
feature_list = []
feat = "Feature"
err_coord = []

# CRS: WGS84
crs_typ = {}
crs_typ["Type"] = "name"
crs = {}
crs["name"] = "urn:ogc:def:crs:OGC:1.3:CRS84"
crs_typ["properties"] = crs

for poi in febs:
    feature = {}    
    # Variable    
    name = poi["name"]
    typ = poi["type"]
    url = poi["url"]
    if (type(poi["loc"][1]) == Decimal) and (type(poi["loc"][0]) 
    == Decimal):
        lon = round(poi["loc"][1], 6)
        lat = round(poi["loc"][0], 6)
    else:
        err_coord.append(poi["name"])
        continue
    # Geometry
    feature["type"] = feat
    geom = {}
    geom["type"] = "Point"
    geom["coordinates"] = [lon, lat]
    feature["geometry"] = geom
    # Properties    
    props ={}
    props["name"] = name
    props["type"] = typ
    props["url"] = url
    feature["properties"] = props
    
    feature_list.append(feature)

# Schreibe in Datei
with open("febs_wiki.geojson", "w") as f:
    f.write(dumps({"type": "FeatureCollection",
                     "crs": crs_typ,
                     "features": feature_list}, indent=2) + "\n")

# Fehler in log Datei
print "Schreibe Fehler Datei"
with open("error_log.txt", "w") as f:
    f.write("Links not parseable:\n")
    for err in error_names:
        f.write(err)
        f.write("\n")
    f.write("\nMissing coordinates:\n")
    for err in err_coord:
        f.write(err)
        f.write("\n")

print "...done"