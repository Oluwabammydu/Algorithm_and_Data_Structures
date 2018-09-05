"""
Created on Thu Aug 30 14:17:07 2018

@author: bamise,mmk and emmanuel
"""

class Stack:

   def __init__(self):

      self.items = []

   def is_empty(self):

      return self.items == []

   def push(self, item):

     self.items.append(item)

   def pop(self):

      return self.items.pop()

   def peek(self):

     return self.items[len(self.items)-1]

   def size(self):

      return len(self.items)



def main():
    pass


if __name__ == '__main__':
    main()
