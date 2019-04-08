import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        l = [1, 2, 3]
        self.assertEqual(max_list_iter(l), 3)
        l = [1, 3, 2]
        self.assertEqual(max_list_iter(l), 3)
        l = [3, 2, 1]
        self.assertEqual(max_list_iter(l), 3)
        self.assertEqual(max_list_iter([]), None)
        l = [1.2, 3.2, 6.9]
        self.assertAlmostEqual(max_list_iter(l), 6.9)
        l = [1.2, 6.9, 3.2]
        self.assertAlmostEqual(max_list_iter(l), 6.9)
        l = [6.9, 3.2, 1.2]
        self.assertAlmostEqual(max_list_iter(l), 6.9)
        self.assertEqual(max_list_iter([-1, -2]), -1)
        self.assertEqual(max_list_iter([2]), 2)


    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertAlmostEqual(reverse_rec([1.1, 2.2, 3.3]), [3.3, 2.2, 1.1])
        self.assertEqual(reverse_rec([13, -3, 0]), [0, -3, 13])
        with self.assertRaises(ValueError):
            reverse_rec(None)
        self.assertEqual(reverse_rec([]), [])
        self.assertEqual(reverse_rec([-1]), [-1])
        self.assertEqual(reverse_rec([-1, -2, -3]), [-3, -2, -1])


    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )
        l = [2, 4, 5, 9]
        low = 0
        high = 3
        self.assertEqual(bin_search(5, low, high, l), 2)
        l = [1, 2, 7, 9]
        self.assertEqual(bin_search(1, 0, 2, l), 0) 
        self.assertEqual(bin_search(2, 0, 0, []), None)
        with self.assertRaises(ValueError):
            bin_search(0, 0, 0, None)
        self.assertAlmostEqual(bin_search(1.3, 0, 3, [1.1, 1.2, 1.3, 1.4]), 2) 
        self.assertEqual(bin_search(2, 0, 0, [2]), 0)    
        self.assertEqual(bin_search(4, 1, 2, [1, 2, 3, 4, 5]), None)
        self.assertEqual(bin_search(0, 2, 3, [0, 1, 2, 3, 4, 5]), None)
        self.assertAlmostEqual(bin_search(.2, 0, 3, [.2, .4, .7, .9]), 0)
        self.assertEqual(bin_search(3, 0, 3, [1, 2, 4, 5]), None)


if __name__ == "__main__":
        unittest.main()

    
