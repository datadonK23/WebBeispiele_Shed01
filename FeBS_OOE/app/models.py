"""
Models
"""

from app import connection

def get_data(con = connection):
    coll = con.BSOOE.febs
    data = coll.find_one({"name": "Schloss Windhaag"})
    return data
