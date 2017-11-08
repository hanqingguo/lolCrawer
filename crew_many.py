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
# true match record no duplicate


summoner = db.summoner
#summoner information
def get_one_summoner_matchid():
#    print(len(db.match.distinct('matches.gameId')))
    return db.match_list.distinct('matches.gameId')


def insert_every_specific_match_of_one_summoner(users):

    for i in range(len(get_one_summoner_matchid())):

        match_record.insert_one(users.get_match(get_one_summoner_matchid()[i]))

def insert_every_specific_match_of_one_summoner_to_record1(users):

    for i in range(len(get_one_summoner_matchid())):

        match_record1.insert_one(users.get_match(get_one_summoner_matchid()[i]))
#    print(db.match_record.distinct('participantIdentities.player.summonerName'))

def get_exist_summonerName():
    return db.match_record.distinct('participantIdentities.player.summonerName')

def save_10000_match_record():
    users_list=['zzzAaronzzz']
    # while(match_record1.count()<10000):
    #
    #
    #     if(len(get_exist_summonerName())<500):
    #         for i in range(len(users_list)):
    #             print("Crew summoner",users_list[i])
    #             users = craw.craw_one(region='na1',summoner_name=users_list[i])
    #             match_list.insert_one(users.get_match_list())
    #             insert_every_specific_match_of_one_summoner(users)
    #
    #             for j in range(len(get_exist_summonerName())):
    #                 users_list.append(get_exist_summonerName()[j])
    #                 print("The length of users_list is",len(users_list))
    #                 print("The length of no duplicate user list is", len(get_exist_summonerName()))
    #                 print(get_exist_summonerName())
    #
    #     else:
    print("Begin collect no duplicate Record")
    for k in range(len(get_exist_summonerName())):
        print("Truely Crew summoner for No duplicate Record",get_exist_summonerName()[k+2])
        try:
            player=craw.craw_one(region='na1',summoner_name=get_exist_summonerName()[k+2])
            insert_every_specific_match_of_one_summoner_to_record1(player)
        except urllib.error.HTTPError:
            print("Client not found")





            # if(len(users_list)<500):
            #     a=get_exist_summonerName()
            #     for j in range(len(a)):
            #     # append our user list
            #         if j<len(a)-1:
            #             users_list.append(get_exist_summonerName()[j+1])
            #             print("add new summonerName",get_exist_summonerName()[j+1])
            #     print("users_list length:",len(users_list))

save_10000_match_record()




