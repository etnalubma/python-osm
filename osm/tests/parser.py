import unittest
from osm.parser import OSMFile
import os
def tearDown(self): 
    pass

class OSMFileTest(unittest.TestCase):
    def setUp(self):
        self.file1 = OSMFile(os.path.dirname(__file__)+"/sample1.xml")

    def test_import(self):
        self.failIfEqual(self.file1, None)
    
    def test_nodes(self):
        self.assertEqual(len(self.file1.nodes), 10)
        self.assertEqual(self.file1.nodes[0].tags, 
                        {
                            u'shop': u'books', 
                            u'opening_hours': u'Mo-Fr 08:30-20:00', 
                            u'name': u'Library Test'
                        })
        self.assertEqual(self.file1.nodes[1].tags, {})
    
    def test_ways(self):
        #self.assertEqual(len(self.file1.ways), 3)
        self.assertEqual(self.file1.ways[0].tags, 
                        {
                            u'highway': u'primary',
                            u'name': u'Test Avenue',
                            u'maxspeed': u'30',
                            u'lanes': u'2'
                        })


