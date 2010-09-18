
class Node(object):
    """
    This module creates a node:
     >>> from osm.objects import Node
     >>> n = Node(12, lon=1.5, lat=1.7, tags= {'name':'point1'}) 
     >>> repr(n)
     "Node(id=12, lon=1.5, lat=1.7, tags={'name': 'point1'})"
    
    """
    def __init__(self, id=None, lon=None, lat=None, tags={}):
        self.id = id
        self.lon, self.lat = lon, lat
        self.tags = tags

    def __repr__(self):
        return "Node(id=%r, lon=%r, lat=%r, tags=%r)" % (self.id, self.lon, self.lat, self.tags)

class Way(object):
    def __init__(self, id, nodes=[], tags={}):
        self.id = id
        self.nodes = nodes
        self.tags = tags

    def __repr__(self):
        return "Way(id=%r, nodes=%r, tags=%r)" % (self.id, self.nodes, self.tags)

class NodePlaceHolder(object):
    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return "NodePlaceHolder(id=%r)" % (self.id)
