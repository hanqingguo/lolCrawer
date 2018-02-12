__author__ = 'hanqing'

from lolCrawer import craw
import pymongo
import urllib.request

client1 = pymongo.MongoClient('localhost', 27017)
db = client1.PlayerRecord

match_list=db.matchList
player_list=db.playerList
player_record=db.playerRecord
clean_record=db.cleanPlayer

#users_list=['zzzAaronzzz']

def get_one_summoner_matchid():
#    print(len(db.match.distinct('matches.gameId')))
    return db.matchList.distinct('matches.gameId')

def uniqueList(list1):
    myset=set(list1)
    newlist=list(myset)
    return newlist

def findPlayerId_inMatch(name,match):
    id=0
    for i in range(len(match['participantIdentities'])):
        if(name==match['participantIdentities'][i]['player']['summonerName']):
            id=match['participantIdentities'][i]['participantId']

    return id

def getWinorLost(match,teamId):
    result='Null'
    if(teamId==100):
        result= match['teams'][0]['win']
    else:
        result=match['teams'][1]['win']

    return result


def getAverageInfo(matchArr):
    total={
        'TotalDamage':0,
        'TotalWinRate':0,
        'TotalKill':0,
        'TotalDeath':0,
        'TotalAssist':0,
        'TotalDamageToken':0,
        'TotalMoney':0
        }

    for i in range(len(matchArr)):
        total['TotalDamage']+=matchArr[i]['performance']['totalDamageDealtToChampions']
        if(matchArr[i]['performance']['win']):
            total['TotalWinRate']+=1
        total['TotalKill']+=matchArr[i]['performance']['kills']
        total['TotalDeath']+=matchArr[i]['performance']['deaths']
        total['TotalAssist']+=matchArr[i]['performance']['assists']
        total['TotalDamageToken']+=matchArr[i]['performance']['totalDamageTaken']
        total['TotalMoney']+=matchArr[i]['performance']['goldEarned']
        #total['TotalWards']+=matchArr[i]['performance']['wardsPlaced']
    print(total)
    return total


def get_100playerlist():
    users_list=['zzzAaronzzz']
    while(len(users_list)<101):
        for k in range(len(users_list)):
            player=craw.craw_one(region='na1',summoner_name=users_list[k])
            match_list.insert_one(player.get_match_list())
            list=get_one_summoner_matchid()
            print(list)
            for i in range(len(list)):
                match=player.get_match(list[i])
                for j in range(len(match['participantIdentities'])):
                    users_list.append(match['participantIdentities'][j]['player']['summonerName'])
            users_list=uniqueList(users_list)
            print(len(users_list))
    playerlist={"playerlist":users_list}
    player_list.insert_one(playerlist)


def get_100playerRecord():
    users_list1=player_list.distinct('playerlist')
    users_list=users_list1[70:]
    for i in range(len(users_list)):
        player=craw.craw_one(region='na1',summoner_name=users_list[i])
        matches=player.get_match_list()
        matchlist=[]
        matchArr=[]
        for j in range(len(matches['matches'])):
            matchlist.append(matches['matches'][j]['gameId'])
        for k in range(len(matchlist)):
            matchDetail=player.get_match(matchlist[k])
            id=findPlayerId_inMatch(users_list[i],matchDetail)
            index=id-1
            highestRank=matchDetail['participants'][index]['highestAchievedSeasonTier']
            teamId=matchDetail['participants'][index]['teamId']
            win_or_lost=getWinorLost(matchDetail,teamId)
            performance=matchDetail['participants'][index]['stats']

            matchPerformance={'MatchId':str(matchlist[k]),'win':win_or_lost,'performance':performance}
            matchArr.append(matchPerformance)

        total=getAverageInfo(matchArr)

        AverageDamage=total['TotalDamage']/20
        AverageWinRate=total['TotalWinRate']/20
        AverageKill=total['TotalKill']/20
        AverageDeath=total['TotalDeath']/20
        AverageAssist=total['TotalAssist']/20
        AverageDamageToken=total['TotalDamageToken']/20
        AverageMoney=total['TotalMoney']/20


        record={'playerName':users_list[i],'highestRank':highestRank,'match_performance':matchArr}


        record1={'playerName':users_list[i],'highestRank':highestRank,'AverageDamage':AverageDamage,'AverageWinRate':AverageWinRate
        ,'AverageKill':AverageKill,'AverageDeath':AverageDeath,'AverageAssist':AverageAssist,'AverageDamageToken':AverageDamageToken,
             'AverageMoney':AverageMoney}

        player_record.insert_one(record)
        clean_record.insert_one(record1)



#get_100playerlist()
get_100playerRecord()






