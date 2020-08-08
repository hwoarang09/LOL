#!/usr/bin/env python
# coding: utf-8

# In[1]:



import requests


itemlink='http://ddragon.leagueoflegends.com/cdn/10.15.1/data/en_US/item.json'
r=requests.get(itemlink)
item=r.json()
ikl=list(item['data'].keys())

def item_key_trans(input):
    if type(input)==str:
        return itemname_to_key(input)
    elif type(input)==int:
        return key_to_itemname(input)
def itemname_to_key(itname):
    for a in range(0,len(item['data'])):
        itemname=(item['data'][ikl[a]]['name'])
        if itemname==itname:
            return (ikl[a])
def key_to_itemname(key):
    name=item['data'][str(key)]['name']
    return (name)    


# In[ ]:




