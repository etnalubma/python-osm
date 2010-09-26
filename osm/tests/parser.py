import unittest
from osm.parser import OSMXMLFile
from osm.objects import Node
import os

class OSMXMLFileTest(unittest.TestCase):
    def setUp(self):
        self.file1 = OSMXMLFile(os.path.dirname(__file__)+"/sample1.xml")

    def test_import(self):
        self.failIfEqual(self.file1, None)
    
    def test_nodes(self):
        self.assertEqual(len(self.file1.nodes), 10)
        self.assertEqual(self.file1.nodes[-1].tags, {})        
        self.assertEqual(self.file1.nodes[-10].tags, 
                        {
                            u'shop': u'books', 
                            u'opening_hours': u'Mo-Fr 08:30-20:00', 
                            u'name': u'Library Test'
                        })

    
    def test_ways(self):
        self.assertEqual(len(self.file1.ways), 3)
        self.assertEqual(self.file1.ways[-13].tags, {})        
        self.assertEqual(self.file1.ways[-11].tags, 
                        {
                            u'highway': u'primary',
                            u'name': u'Test Avenue',
                            u'maxspeed': u'30',
                            u'lanes': u'2'
                        })

    def test_way_nodes(self):
        self.assertEqual(len(self.file1.ways[-11].nodes), 4)
        self.assertEqual(len(self.file1.ways[-13].nodes), 3)
        self.assertEqual(self.file1.nodes[-1], self.file1.ways[-11].nodes[0])
        self.assertEqual(self.file1.nodes[-4], self.file1.ways[-11].nodes[3])
        
    def test_relations(self):
        self.assertEqual(len(self.file1.relations), 1)
    
    
    
