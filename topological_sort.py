# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 17:20:27 2018

@author: Bammydu and Posh
"""

#Depth first search function

def iterative_dfs(graph, start):
    seen = set()
    path = []
    q = [start]
    while q:
        v = q.pop()
        if v not in seen:
            seen.add(v)
            path.append(v)
            q.extend(graph[v]) 
        '''This will add the nodes in a slightly different
           order for the same order, use reversed(graph[v])
        '''

    return path
graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['d'],
    'd': ['e'],
    'e': []
}

print(iterative_dfs(graph, 'a'))


'''
Modifying the depth first search function to produce a topological sort
'''
def iterative_topological_sort(graph, start):
    seen = set()
    stack = []
    order = []
    q = [start]
    while q:
        v = q.pop()
        if v not in seen:
            seen.add(v) 
            q.extend(graph[v])

            while stack and v not in graph[stack[-1]]:
                order.append(stack.pop())
            stack.append(v)

    return stack + order[::-1]   

graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['d'],
    'd': ['e'],
    'e': []
}
print(iterative_topological_sort(graph, 'a'))