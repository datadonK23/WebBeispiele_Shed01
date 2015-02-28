# -*- coding: utf-8 -*-
"""
Scrape Wikipedia Article
Purpose: Scrape list of castles in Upper Austria and get Name, Geo-Coordinates
         and Type
@author: Thomas Treml (datadonk23@gmail.com)
Date: 28.02.2015
"""

import wikipedia
from bs4 import BeautifulSoup

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

# Extrahiere Name und Koordinaten aus jedem Link und logge Fehler
for i in range(len(urls)):
    print "processing #" + str(i) + " from " + str(len(urls))
    try:
        page_pointer = wikipedia.page(urls[i][6:])
        features = {}
        features["name"] = page_pointer.title
        try:
            features["loc"] = page_pointer.coordinates
        except:
            features["loc"] = ["0", "0"]
        if "urg" in features["name"]: # REGEX
            features["type"] = "Burg"
        elif "chlo" in features["name"]:
            features["type"] = "Schloss"
        else:
            features["type"] = "undef"
        febs.append(features)
    except wikipedia.exceptions.PageError:
        error_name = urls[i][6:]
        error_names.append(error_name)
    i+=1

print "Schreibe Ergebnis Datei"

# Ergebnisse zu txt
with open("save_result.txt", "w") as f:
    for obj in febs:
        f.write(str(obj))
        f.write("\n")

print "Schreibe Fehler Datei"

# Fehler zu txt
with open("save_errors.txt", "w") as f:
    for err in error_names:
        f.write(err)
        f.write("\n")

