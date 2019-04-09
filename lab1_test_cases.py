import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        #check value error
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        l = [1, 2, 3]
        #check each place of list for positive numbers
        self.assertEqual(max_list_iter(l), 3)
        l = [1, 3, 2]
        #check each place of list for positive numbers
        self.assertEqual(max_list_iter(l), 3)
        l = [3, 2, 1]
        #check each place of list for positive numbers
        self.assertEqual(max_list_iter(l), 3)
        #check empty list
        self.assertEqual(max_list_iter([]), None)
        l = [1.2, 3.2, 6.9]
        #check each place of list for decimals
        self.assertAlmostEqual(max_list_iter(l), 6.9)
        l = [1.2, 6.9, 3.2]
        #check each place of list for decimals 
        self.assertAlmostEqual(max_list_iter(l), 6.9)
        l = [6.9, 3.2, 1.2]
        #check each place of list for decimals 
        self.assertAlmostEqual(max_list_iter(l), 6.9)
        #check list with negative numbers
        self.assertEqual(max_list_iter([-1, -2]), -1)
        #check list with negative numbers
        self.assertEqual(max_list_iter([-2, -1]), -1)
        #check list with one number
        self.assertEqual(max_list_iter([2]), 2)


    def test_reverse_rec(self):
        #reverse list of positive numbers
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        #reverse list of decimals 
        self.assertAlmostEqual(reverse_rec([1.1, 2.2, 3.3]), [3.3, 2.2, 1.1])
        #reverse list with a negative number
        self.assertEqual(reverse_rec([13, -3, 0]), [0, -3, 13])
        #raise value error
        with self.assertRaises(ValueError):
            reverse_rec(None)
        #empty list
        self.assertEqual(reverse_rec([]), [])
        #reverse list with one number
        self.assertEqual(reverse_rec([-1]), [-1])
        #reverse list with all negative numbers
        self.assertEqual(reverse_rec([-1, -2, -3]), [-3, -2, -1])


    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        #find number in the middle of the list
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )
        l = [2, 4, 5, 9]
        low = 0
        high = 3
        #check left hand side of list
        self.assertEqual(bin_search(5, low, high, l), 2)
        l = [1, 2, 7, 9]
        #check when the high value cuts off part of the list
        self.assertEqual(bin_search(1, 0, 2, l), 0) 
        #check empty list
        self.assertEqual(bin_search(2, 0, 0, []), None)
        #raise value error
        with self.assertRaises(ValueError):
            bin_search(0, 0, 0, None)
        #check right hand side of a list of decimals
        self.assertAlmostEqual(bin_search(1.3, 0, 3, [1.1, 1.2, 1.3, 1.4]), 2)
        #check list with one value 
        self.assertEqual(bin_search(2, 0, 0, [2]), 0)   
        #check when high and low value cuts off value from list on right 
        self.assertEqual(bin_search(4, 1, 2, [1, 2, 3, 4, 5]), None)
        #check when high and low value cuts off value from list on left
        self.assertEqual(bin_search(0, 2, 3, [0, 1, 2, 3, 4, 5]), None)
        #check list of decimals
        self.assertAlmostEqual(bin_search(.2, 0, 3, [.2, .4, .7, .9]), 0)
        #check when the value isn't in list
        self.assertEqual(bin_search(3, 0, 3, [1, 2, 4, 5]), None)
        #check list with negative
        self.assertEqual(bin_search(-2, 0, 4, [-5, -4, -3, -2, -1]), 3)


if __name__ == "__main__":
        unittest.main()

    
