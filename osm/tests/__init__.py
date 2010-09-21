import doctest
import unittest
from osm import objects
from osm.tests.parser import OSMFileTest
    
def suite():
    optionflags = doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS
    globs = {}

    suite = unittest.TestSuite()
    
    suite.addTest(doctest.DocTestSuite(
       objects,
        optionflags=optionflags,
        globs=globs
    ))
        
    suite.addTest(unittest.makeSuite(OSMFileTest))
    
    return suite
    

