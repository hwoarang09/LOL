#!/usr/bin/env python
# coding: utf-8

# In[8]:


import requests
from pandas.io.json import json_normalize
import requests
import pandas as pd
import numpy as np
import time
from pandas.io.json import json_normalize
import requests
import pandas as pd
import numpy as np
import time
import pandas as pd
import pickle

#Self Created Modules
#############################################################################
from champ_key_trans import champ_key_trans as ckt

#############################################################################





def gameId_main(summonerName, championName, apikey):
    api_key=apikey

    
    

    def gameId_get(en_id,champion):
        gameId_list = []


        aa=int((totalGames)/100)
        k=0
        while k<=aa:
            #print(k*100,'부터 ', (k+1)*100, '까지')

            endindex=(k+1)*100
            startindex=k*100
            matchlist = ('https://kr.api.riotgames.com/lol/match/v4/matchlists/by-account/'+ en_id + 
                         '?champion='+str(ckt(champion))+'&queue=420&endIndex='+str(endindex)+'&beginIndex='+str(startindex)+
                         '&api_key='+api_key)
            R_matchlist = requests.get(matchlist)

            #print(startindex, endindex)
            try:
                for a in range(0, totalGames-startindex):
                    #gameId_list.append(R_matchlist.json()['matches'][a]['gameId'])
                    if (R_matchlist.json()['matches'][a]['queue']==420):
                        gameId_list.append(R_matchlist.json()['matches'][a]['gameId'])
                        #print(R_matchlist.json()['matches'][a]['queue'], R_matchlist.json()['matches'][a]['gameId'])




                    while R_matchlist.status_code == 429:
                        time.sleep(5)
                        print('429error......쉬엇다간다1')
                        #gameId_list.append(R_matchlist.json()['matches'][a]['gameId'])
                        if (R_matchlist.json()['matches'][a]['queue']==420):
                            gameId_list.append(R_matchlist.json()['matches'][a]['gameId'])


            except:
                pass
            k+=1




        print(len(gameId_list), "  :  ", totalGames)        
        return gameId_list





    def id_timeline_SUM(summoner):
        list_id_timeline_SUM = []
        #for i in range(0, len(summoner):
        for i in range(0, 5):
            gameId_one=summoner[i]
            list_id_timeline={}
            list_id_timeline['gameId']=gameId_one
            try:

                match_Id='https://kr.api.riotgames.com/lol/match/v4/matches/' +str(gameId_one)+'?api_key=RGAPI-862490fb-0ebd-4b90-b7b7-7eadec9c2300'
                R_match_Id=requests.get(match_Id)
                list_id_timeline['match_Id'] = R_match_Id.json()
            except:
                while R_match_Id.status_code == 429:
                    time.sleep(5)
                    print('429error......쉬엇다간다1')
                    gameId_one=list_gameId[0][1][i]
                    match_Id='https://kr.api.riotgames.com/lol/match/v4/matches/' +str(gameId_one)+'?api_key=RGAPI-862490fb-0ebd-4b90-b7b7-7eadec9c2300'
                    R_match_Id=requests.get(match_Id)
                list_id_timeline['match_Id'] = R_match_Id.json()



            try:
                match_timeline='https://kr.api.riotgames.com/lol/match/v4/timelines/by-match/' +str(gameId_one)+'?api_key=RGAPI-862490fb-0ebd-4b90-b7b7-7eadec9c2300'
                R_match_timeline=requests.get(match_timeline)
                list_id_timeline['match_timeline']=R_match_timeline.json()
            except:
                while R_match_timeline.status_code == 429:
                    time.sleep(5)
                    print('429error......쉬엇다간다1')
                    match_timeline='https://kr.api.riotgames.com/lol/match/v4/timelines/by-match/' +str(gameId_one)+'?api_key=RGAPI-862490fb-0ebd-4b90-b7b7-7eadec9c2300'
                    R_match_timeline=requests.get(match_timeline)
                list_id_timeline['match_timeline']=R_match_timeline.json()


            list_id_timeline_SUM.append(list_id_timeline)
        return list_id_timeline_SUM
    
    
    list_gameId = []

    list_imsi =[]

    try:
        summoner_name=summonerName
        print(summoner_name)
        sohwan = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" +summoner_name+'?api_key=' + api_key
        R_sohwan = requests.get(sohwan)
        print("encrypted accountID : ", R_sohwan.json()['accountId'])


        #get totalGames (RankSolo)
        en_summoner_id=R_sohwan.json()['id']
        sohwan2=('https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/'+en_summoner_id+ '?api_key='+ api_key)
        R_sohwan2 = requests.get(sohwan2)
        print("ID : ", R_sohwan2.json()[0]['summonerName'])
        print("wins : ", R_sohwan2.json()[0]['wins'])
        print("losses : ", R_sohwan2.json()[0]['losses'])
        print("Games play  : ", R_sohwan2.json()[0]['wins'] + R_sohwan2.json()[0]['losses'], '\n')
        totalGames=R_sohwan2.json()[0]['wins'] + R_sohwan2.json()[0]['losses']

        #get gameId list, playes by the champion
        list_imsi.append(R_sohwan2.json()[0]['summonerName'])
        list_imsi.append(gameId_get(R_sohwan.json()['accountId'], championName))



    except:
        while (R_sohwan.status_code == 429)or (R_sohwan2.status_code == 429):
            time.sleep(5)
            summoner_name=summonerName
            print(summoner_name)
            sohwan = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" +summoner_name+'?api_key=' + api_key
            R_sohwan = requests.get(sohwan)
            print("encrypted accountID : ", R_sohwan.json()['accountId'])


            #get totalGames (RankSolo)
            en_summoner_id=R_sohwan.json()['id']
            sohwan2=('https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/'+en_summoner_id+ '?api_key='+ api_key)
            R_sohwan2 = requests.get(sohwan2)
            print("ID : ", R_sohwan2.json()[0]['summonerName'])
            print("wins : ", R_sohwan2.json()[0]['wins'])
            print("losses : ", R_sohwan2.json()[0]['losses'])
            print("Games play  : ", R_sohwan2.json()[0]['wins'] + R_sohwan2.json()[0]['losses'], '\n')
            totalGames=R_sohwan2.json()[0]['wins'] + R_sohwan2.json()[0]['losses']

            #get gameId list, playes by the champion
            list_imsi.append(R_sohwan2.json()[0]['summonerName'])
            list_imsi.append(gameId_get(R_sohwan.json()['accountId'], championName))

        print("No Summoner : ", summoner_name, "\n")
        pass
    list_gameId.append(list_imsi)
    list_imsi=[]



    return list_gameId[0]

