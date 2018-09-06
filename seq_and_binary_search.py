# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 17:04:25 2018

@author: OLUWABAMISE AND ZOKKY
"""

import time
start = time.time()
def bisect_algo(item, testlist):
    first = 0
    last = len(testlist) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last)// 2
        if testlist[midpoint] == item:
            found = True
        else:
            if testlist[midpoint] > item:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found

newlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(bisect_algo(17, newlist))
end = time.time()
print(end - start)

start = time.time()
def sequential_search(a_list, item):
    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos+1
    return found
test_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequential_search(test_list, 13))
end = time.time()
print(end - start)

"""
True
0.0
Above result is for the Binary search that yielded its result in 0.0 seconds.  

True
0.003998756408691406
Result for Sequential search.

The Binary search was faster. 
"""