import doctest
import unittest
from osm import objects

def setUp(self):
    pass
     
def tearDown(self): 
    pass
    
def suite():
    optionflags = doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS
    globs = {}

    suite = unittest.TestSuite()
    
    suite.addTest(doctest.DocTestSuite(
       objects,
        optionflags=optionflags,
        setUp=setUp,
        tearDown=tearDown,
        globs=globs
    ))
        
    return suite
    

