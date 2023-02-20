#!/usr/bin/env python
# coding: utf-8

# This is used as an example of creating and importing modules.

# In[ ]:

test = "Today is the best day of my life."
# Morgan's library module
x = 2
y = 4
print(x+y)

def find_index(lst,itm):#lst,itm: List and Item to be searched
    try:
        index = lst.index(itm)
        return index
    except ValueError as ve:
        return(f'{itm}, is not in the list.')