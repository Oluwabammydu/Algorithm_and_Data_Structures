"""
Created on Thu Aug 30 14:17:07 2018

@author: bamise,mmk and emmanuel
"""

import Problem2DataStructures as p
import unittest


class TestProblem1DataStructures(unittest.TestCase):
     """
    Test if the file exist and also test if the html are tag properly
    """

     def test_file_exist(self):
        """
        Test that the file exist return True if it's exist or False if not.
        """
        file_name="HTMLDOC.txt"
        result = p.file_exist(file_name)
        self.assertTrue(result,True)

     def test_is_html_tag_properly(self):

        """
        Test that the html document is properly tag(we assumed that the file is not a binary file).
        """
        file="HTMLDOC.txt"
        html_doc=p.read_file(file)
        result=p.is_html_tag_properly(html_doc)
        self.assertTrue(result,True)




if __name__ == '__main__':
    unittest.main()