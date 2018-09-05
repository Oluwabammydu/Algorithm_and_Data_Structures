# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 15:01:04 2018

@author: OLUWABAMISE AND ZOKKY
"""

def reverse_ls(ls):
    if len(ls) == 0:
        return []
    else:
        return [ls[-1]] + reverse_ls(ls[:1])
lists = [3,6,5,8,10]
print(reverse_ls(lists))