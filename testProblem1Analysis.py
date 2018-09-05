# -*- coding: utf-8 -*-
"""
Created on Tue Aug  29 14:00:32 2018

@author: OLUWABAMISE, MMK AND EMMANUEL 
"""

import Problem1Analysis
import unittest


class TestProblem1Analysis(unittest.TestCase):
     """
    Test the smallest_num_unsorted_list() function from the Problem1Analysis library
    """
     def test_smallest_num_unsorted_list(self):
        """
        Test that the unsorted list  returns the smallest number in the list
        """
        result = Problem1Analysis.smallest_num_unsorted_list([5,7,9,8,4,66,78,45,3,90,62])
        self.assertEqual(result, 3)





if __name__ == '__main__':
    unittest.main()