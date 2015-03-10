"""
Models
"""

from app import connection

class Features:
    """
    Features from DB
    """
    def __init__(self, connection):
        self.connection = connection

    def get_burgen(self):
        coll = connection.BSOOE.febs
        burgen = coll.find({"type": "Burg"})
        return burgen

    def get_schloesser(self):
        coll = connection.BSOOE.febs
        schloesser = coll.find({"type": "Schloss"})
        return schloesser
    
    def get_unbekannt(self):
        coll = connection.BSOOE.febs
        unbekannte = coll.find({"type": "unb"})
        return unbekannte
    
    def get_nearest(self, myCoords=[13.964049, 48.136443]):
        coll = connection.BSOOE.febs
        nearest_list = []
        myLoc = {"$geometry":{"type":"Point", "coordinates": myCoords}}
        query = coll.find({"loc": {"$near": myLoc}}).limit(3)
        for doc in query:
            nearest_list.append(doc)
        return nearest_list
        
    def get_boundaries(self):
        coll = connection.BSOOE.bound
        state_boundary = coll.find({"name": "state_boundary"})
        return state_boundary
