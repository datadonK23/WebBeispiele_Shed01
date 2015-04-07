# -*- coding: utf-8 -*-
"""
Track Model

@author: Thomas Treml (datadonk23@gmail.com)
Date: 24.02.2015
"""

import json

with open("tracks.geojson") as f:
    data = json.load(f)

for feature in data["features"]:
    print feature["properties"]["name"]
    print feature["properties"]["len"]    
    print feature["geometry"]["coordinates"]
