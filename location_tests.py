import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
        loc = Location("Paris", 1, 2)
        self.assertEqual(repr(loc), "Location('Paris', 1, 2)")
    # Add more tests!
    #def test_init(self, name, lat, lon):
        #self.assertAlmostEqual(init("Paris",   

    def test_eq(self):
        loc1 = Location("SLO", 3, 4)
        loc2 = Location("Italy", -5, 4.5)
        loc3 = loc1
        loc4 = Location("Italy", -5, 4.5)
        self.assertFalse(loc1 == loc2)
        self.assertTrue(loc2 == loc4)
        self.assertTrue(loc1 == loc3)


if __name__ == "__main__":
        unittest.main()
