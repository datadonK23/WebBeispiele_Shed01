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
        
    def get_boundaries(self):
        coll = connection.BSOOE.bound
        state_boundary = coll.find({"name": "state_boundary"})
        return state_boundary
