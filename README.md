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
    player.get_match_list()
    
### Craw_many.py use one summoner name as seed, recursively collect 10000 match to mongoDB.

### MongoDB

#### Installation
    
    https://docs.mongodb.com/manual/installation/

Install pymongo to drive mongoDB

    $ python -m pip install pymongo

#### Connect mongoDB

    1. Start DB
    2. Connect MongoDB
    
    import pymongo
    client1 = pymongo.MongoClient('localhost', 27017)  
    db = client1.LOLRecord3                                 ### DB name is LOLRecord3
    match_record = db.match_record                          ### collection name is match_record
    match_record.insert_one(player.get_match_list)          ### Save match list to collection match_record                 
    
### Visualization

#### [pieChart1](https://hanqingguo.github.io/lolCrawer/visulation/bad_piechart.html)
#### [pieChart2](https://hanqingguo.github.io/lolCrawer/visulation/sun_brust.html)

#### [barChart](https://hanqingguo.github.io/lolCrawer/visulation/bar_chart_bad.html)

#### [networkChart](https://hanqingguo.github.io/lolCrawer/visulation/good_network.html)

