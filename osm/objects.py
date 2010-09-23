
class Node(object):
    """
    Node Object
    -----------
    
    >>> from osm.objects import Node
    >>> n = Node(12, lon=1.5, lat=1.7, tags= {'name':'point1'}) 
    >>> repr(n)
    "Node(id=12, lon=1.5, lat=1.7, tags={'name': 'point1'})"
    
    """

    def __init__(self, id, lon=None, lat=None, tags=None):
        self.id = id
        self.lon, self.lat = lon, lat
        if tags:
            self.tags = tags
        else:
            self.tags = {}

    def __repr__(self):
        return "Node(id=%r, lon=%r, lat=%r, tags=%r)" % (self.id, self.lon, self.lat, self.tags)

class Way(object):
    """
    Way Object
    -----------
    
    >>> from osm.objects import Way
    >>> w = Way(15, tags={'name':'way1'})
    >>> repr(w)
    "Way(id=15, nodes=[], tags={'name': 'way1'})"
    
    """

    def __init__(self, id, nodes=None, tags=None):
        self.id = id
        if nodes:
            self.nodes = nodes
        else:
            self.nodes = []
        if tags:
            self.tags = tags
        else:
            self.tags = {}

    def __repr__(self):
        return "Way(id=%r, nodes=%r, tags=%r)" % (self.id, self.nodes, self.tags)

class NodePlaceHolder(object):
    """
    NodePlaceHolder Object
    ----------------------
    
    >>> from osm.objects import NodePlaceHolder
    >>> n = NodePlaceHolder(id=2)
    >>> repr(n)
    'NodePlaceHolder(id=2)'
    """
    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return "NodePlaceHolder(id=%r)" % (self.id)

