#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


day1 = open("input_01.txt", "r")
lst = []
for i in day1: 
    lst.append(i.strip())


# In[3]:



values = []
counrt = 0
for ix, val in enumerate(lst):
    if ix == 0:
        continue
        
    else:
        
        if val > lst[ix-1] :
            values.append("increase")
            counrt += 1
            print(lst[ix-1], " ", val, " increase")
        else:
            values.append("decrease")
            print(lst[ix-1], " ", val," decrease")
            
x = values.count("increase")
print(x, counrt)


# In[20]:



values1 = []
counrt = 0
 
    
l = len(lst)
for ix, val in enumerate(lst):
    
    if ix < l-3 :
        
        sum1 = int(val) + int(lst[ix+1]) + int(lst[ix+2])
       # print(val , lst[ix+1] , lst[ix+2], sum1)
        
        values1.append(sum1)
    else:
        if ix == l-3:
            sum1 = int(val) + int(lst[ix+1]) + int(lst[ix+2])
            #print(val , lst[ix+1] , lst[ix+2], sum1)

            values1.append(sum1)
        else:
            continue
            

values2 = []
counrt2 = 0
for ix, val in enumerate(values1):
    if ix == 0:
        continue
        
    else:
        
        if val > values1[ix-1] :
            values2.append("increase")
            counrt += 1
            print(lst[ix-1], " ", val, " increase")
        else:
            values2.append("decrease")
            print(values1[ix-1], " ", val," decrease")
            
x = values2.count("increase")
            

print(x)


# In[ ]:




