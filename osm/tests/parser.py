import unittest
from osm.parser import OSMFile
from osm.objects import Node
import os


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
        self.assertEqual(len(self.file1.ways), 3)
        self.assertEqual(self.file1.ways[0].tags, 
                        {
                            u'highway': u'primary',
                            u'name': u'Test Avenue',
                            u'maxspeed': u'30',
                            u'lanes': u'2'
                        })
        self.assertEqual(self.file1.ways[1].tags, {})

    def test_way_nodes(self):
        ways = dict([(w.id, w) for w in self.file1.ways])
        self.assertEqual(len(ways['-11'].nodes), 4)
        self.assertEqual(len(ways['-13'].nodes), 3)

        nodes = dict([(n.id, n) for n in self.file1.nodes])

        self.assertEqual(nodes['-1'], ways['-11'].nodes[0])
        self.assertEqual(nodes['-4'], ways['-11'].nodes[3])
        
        
