__author__ = 'hanqing'

from lolCrawer import craw
import pymongo
import urllib.request
import pandas as pd
from pandas.io.json import json_normalize

client1 = pymongo.MongoClient('localhost', 27017)
db = client1.PlayerRecord

match_list=db.matchList
player_list=db.playerList
player_record=db.recordList


print(list(player_record.find()))

df = pd.DataFrame(list(player_record.find()))

data=json_normalize(df)
print(data.head())


