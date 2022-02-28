#!/usr/bin/env python
# coding: utf-8

# In[57]:


import numpy as np
import pandas as pd
import bigjson


# In[58]:


count  = 0
#create a dictionary 
references_dict = {'id':[],
                  'title':[],
                  'doc_type':[],
                  'publisher':[],
                  'venue_name':[],
                  'venue_ID':[],
                  'references':[]}
#open file
with open('dblp.v12.json', 'rb') as f:
    #load json into j
    j = bigjson.load(f)
    #load limited number of publications 
    while count<34:
        element = j[count]
        if 'references' in element.keys():
            for i,val in enumerate(element['references']):
                references_dict['references'].append(element['references'][i])
                references_dict['id'].append(element['id'])
                references_dict['title'].append(element['title'])
                if element['publisher'] != "":
                     references_dict['publisher'].append(element['publisher'])
                else:
                     references_dict['publisher'].append(np.nan)
                if element['doc_type'] != "":
                    references_dict['doc_type'].append(element['doc_type'])
                else:
                    references_dict['doc_type'].append(np.nan)
                if 'venue' in element.keys():
                    if 'raw' in element['venue'].keys():
                        references_dict['venue_name'].append(element['venue']['raw'])
                    else:
                        references_dict['venue_name'].append(np.nan)
                    if 'id' in element['venue'].keys():
                        references_dict['venue_ID'].append(element['venue']['id'])
                    else:
                        references_dict['venue_ID'].append(np.nan)
                else:
                    references_dict['venue_name'].append(np.nan)
                    references_dict['venue_ID'].append(np.nan)

        else:
            references_dict['references'].append(np.nan)
            references_dict['id'].append(element['id'])
            references_dict['title'].append(element['title'])
     
   
            
            if element['publisher'] != "":
                references_dict['publisher'].append(element['publisher'])
            else:
                references_dict['publisher'].append(np.nan)
            
            if element['doc_type'] != "":
                    references_dict['doc_type'].append(element['doc_type'])
            else:
                    references_dict['doc_type'].append(np.nan)
            if 'venue' in element.keys():
                if 'raw' in element['venue'].keys():
                    references_dict['venue_name'].append(element['venue']['raw'])
                else:
                    references_dict['venue_name'].append(np.nan)
                if 'id' in element['venue'].keys():
                    references_dict['venue_ID'].append(element['venue']['id'])
                else:
                    references_dict['venue_ID'].append(np.nan)
            else:
                    references_dict['venue_name'].append(np.nan)
                    references_dict['venue_ID'].append(np.nan)
        
        count = count + 1


# In[59]:


data = pd.DataFrame.from_dict(references_dict)


# In[60]:


dropped = data.drop(columns=['id', 'title', 'venue_ID', 'references'])


# In[61]:


dropped.to_csv('Dataset_2_citation_papers.csv', index=False)


# In[ ]:




