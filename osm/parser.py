import xml.sax
from objects import Node, Way, NodePlaceHolder
from copy import deepcopy

class OSMFile(object):
    def __init__(self, filename):
        self.filename = filename
        self.nodes = {}
        self.ways = {}
        self.__parse()

    def __parse(self):
        """Parse the given XML file"""
        parser = xml.sax.make_parser()
        parser.setContentHandler(OSMFileParser(self))
        parser.parse(self.filename)

        # now fix up all the refereneces
        for way in self.ways.values():
            way.nodes = [self.nodes[node_pl.id] for node_pl in way.nodes]

        # convert them back to lists
        self.nodes = self.nodes.values()
        self.ways = self.ways.values()


class OSMFileParser(xml.sax.ContentHandler):
    def __init__(self, containing_obj):
        self.containing_obj = containing_obj
        self.curr_node = None
        self.curr_way = None
        self.curr_tags = {}
    def startElement(self, name, attrs):
        if name == 'node':
            self.curr_node = Node(id=attrs['id'], lon=attrs['lon'], lat=attrs['lat'])
        elif name == 'way':
            self.curr_way = Way(id=attrs['id'])
        elif name == 'tag':
            #import pdb;pdb.set_trace()
            self.curr_tags[attrs['k']] = attrs['v'] 
        elif name == "nd":
            assert self.curr_node is None, "curr_node (%r) is non-none" % (self.curr_node)
            assert self.curr_way is not None, "curr_way is None"
            self.curr_way.nodes.append(NodePlaceHolder(id=attrs['ref']))

    def endElement(self, name):
        if name == "node":
            self.curr_node.tags = deepcopy(self.curr_tags)
            self.containing_obj.nodes[self.curr_node.id] = self.curr_node 
            self.curr_node = None
            self.curr_tags = {}
        elif name == "way":
            self.curr_way.tags = deepcopy(self.curr_tags)
            self.containing_obj.ways[self.curr_way.id] = self.curr_way
            self.curr_way = None
            self.curr_tags = {}
        
