from riotwatcher import RiotWatcher


class craw_one:
    watcher = RiotWatcher('RGAPI-f8a0fee8-7b0c-4ea7-87c1-695bcb030efe')


    def transfer_name_to_summoner(self,region,name):


        me = self.watcher.summoner.by_name(region, name)
        return me

    def __init__(self,region,summoner_name):
        self.summoner_name=summoner_name
        self.region=region
        self.summoner=self.transfer_name_to_summoner(self.region,self.summoner_name)




    def get_region(self):
        return self.region

    def get_summoner(self):
        return self.summoner

    def get_mastery(self):
        my_mastery_pages=self.watcher.masteries.by_summoner(self.region,self.summoner['id'])
        return my_mastery_pages

    def get_match_list(self):
        my_match_list=self.watcher.match.matchlist_by_account_recent(self.region,self.summoner['accountId'])
        return my_match_list

    def get_match(self,matchId):
        my_match=self.watcher.match.by_id(self.region,match_id=matchId)
        return my_match


