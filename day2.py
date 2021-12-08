#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[21]:


data = open("input_02.txt", "r")
cord = []
for i in data: 
    cord.append(i.strip().split())
    
cord


# In[31]:


h = 0
d = 0
a = 0

for i in cord:
    if "forward" in i[0]:
        
        h += int(i[1])
        d += a*int(i[1])
        print(i[0], i[1], d, a)
    else:
        if "down" in i[0]:
            a += int(i[1])
        else:
            a-= int(i[1])
print(h*d)


# In[ ]:




