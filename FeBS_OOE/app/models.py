"""
Models
"""

from app import connection

"""
def get_data(con = connection):
    coll = con.BSOOE.febs
    data = coll.find_one({"name": "Schloss Windhaag"})
    return data
"""

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
        
    def get_boundaries():
        pass
