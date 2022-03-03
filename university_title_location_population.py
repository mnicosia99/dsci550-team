#!/usr/bin/env python
# coding: utf-8

# In[99]:


import json
import pandas as pd
 
# Opening JSON file
f = open('universities_ranking.json')
 
# returns JSON object as
# a dictionary
data = json.load(f)
type(data)

new_dictionary = {}
for ranking in data:
    #print(ranking)
    for key,value in ranking.items():
        #print(key, value)
        if key =='title'or key =='location' or key =='number students':
            #print(key, value)
            new_dictionary[key] = value
    final =new_dictionary
  
    #print(final)
    js = json.dumps(final)
    #print(js)
    

# Open new json file if not exist it will create
    fp = open('dumped.json', 'a')

# write to json file
    fp.write(js)

# close the connection
    fp.close()

    
   


# In[ ]:




