#!/usr/bin/env python
# coding: utf-8

# In[51]:


import requests

champion = "http://ddragon.leagueoflegends.com/cdn/10.15.1/data/en_US/champion.json"
R_champion = requests.get(champion)
x=R_champion.json()['data']
dict_champion_key={}
dict_key_champion={}
for key, value in x.items():
    #print(value['id'], value['key'])
    dict_champion_key[value['id']]=int(value['key'])
    dict_key_champion[int(value['key'])]=value['id']

def champ_key_trans(a):
    if type(a)==int:
        return dict_key_champion[a]
    else:
        return dict_champion_key[a]
        


# In[54]:



    


# In[ ]:




