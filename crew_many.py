from lolCrawer import craw
import pymongo
import urllib.request

client1 = pymongo.MongoClient('localhost', 27017)
db = client1.LOLRecord3

# mastery=db.mastery
# new mastery collection

match_list = db.match_list
# match list collection

match_record = db.match_record
# match collection with all match attributes
match_record1 = db.match_record1



summoner = db.summoner

def get_one_summoner_matchid():
    return db.match_list.distinct('matches.gameId')


def insert_every_specific_match_of_one_summoner(users):

    for i in range(len(get_one_summoner_matchid())):

        match_record.insert_one(users.get_match(get_one_summoner_matchid()[i]))

def insert_every_specific_match_of_one_summoner_to_record1(users):

    for i in range(len(get_one_summoner_matchid())):

        match_record1.insert_one(users.get_match(get_one_summoner_matchid()[i]))


def get_exist_summonerName():
    return db.match_record.distinct('participantIdentities.player.summonerName')

def save_10000_match_record():
    users_list=['zzzAaronzzz']

    print("Begin collect no duplicate Record")
    for k in range(len(get_exist_summonerName())):
        print("Truely Crew summoner for No duplicate Record",get_exist_summonerName()[k+2])
        try:
            player=craw.craw_one(region='na1',summoner_name=get_exist_summonerName()[k+2])
            insert_every_specific_match_of_one_summoner_to_record1(player)
        except urllib.error.HTTPError:
            print("Client not found")



save_10000_match_record()




