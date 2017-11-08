__author__ = 'hanqing'

from lolCrawer import craw
import pymongo
import urllib.request
from pandas import DataFrame

client1 = pymongo.MongoClient('localhost', 27017)
db = client1.PlayerRecord

player_record=db.recordList
clean_record=db.cleanPlayer

df = DataFrame(list(clean_record.find()))
print(df.head())
