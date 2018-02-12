# League of Legend

## Overview

This project collect 10000 records of match history, save it to mongo DB, then extract them and trying to find out useful 

data in this game.

### [Riot Api](#riot-api)

### [Crawl Script](#Craw)

### [MongoDB](#mongo)

### [Visualization](#visualization)

### Riot Api

#### Installation

    pip install riotwatcher

#### Use it!
    
    my_region = 'na1'
    watcher = RiotWatcher('RGAPI-f8a0fee8-7b0c-4ea7-87c1-695bcb030efe')
    me = watcher.summoner.by_name(my_region, 'zzzAaronzzz')
    
HERE "me" is a summoner object

#### Get 20 MATCH HISTORY OF THIS SUMMONER!

    watcher.match.matchlist_by_account_recent(my_region,me['accountId'])

### Crawl Script

craw.py encapsuled riotwatcher api, when give it a summoner name and region, it can use all riotwatcher api by this script.

    class craw_one:
    watcher = RiotWatcher('RGAPI-f8a0fee8-7b0c-4ea7-87c1-695bcb030efe')


    def transfer_name_to_summoner(self,region,name):


        me = self.watcher.summoner.by_name(region, name)
        return me

    def __init__(self,region,summoner_name):
        self.summoner_name=summoner_name
        self.region=region
        self.summoner=self.transfer_name_to_summoner(self.region,self.summoner_name)

#### Once initilized a summoner, then can use methods in craw_one.
    player = craw_one('na1','zzzAaronzzz')
    player.get........
   
