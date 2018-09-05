# -*- coding: utf-8 -*-
"""
Created on Tue Aug  29 14:22:19 2018

@author: OLUWABAMISE, MMK AND EMMANUEL
"""

def smallest_num_unsorted_list(unsortlist):

    '''smallest_num_unsorted_list([3,4,5])  and return the smallest number
      A function  that finds the smallest number in an unsorted list in
      O(nlog(n))'''

    #sort() is used because the Big-O for a sort() in a list is O(nlog(n))
    unsortlist.sort()


    return  unsortlist[0]