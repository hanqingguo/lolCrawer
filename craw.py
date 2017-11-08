from riotwatcher import RiotWatcher


class craw_one:
    watcher = RiotWatcher('RGAPI-f8a0fee8-7b0c-4ea7-87c1-695bcb030efe')


    def transfer_name_to_summoner(self,region,name):


        me = self.watcher.summoner.by_name(region, name)
        print(me)
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

#     def
#     my_region = 'na1'
#
#
#     print(me)
#
# # all objects are returned (by default) as a dict
# # get my 1 mastery page i keep changing
#     my_mastery_pages = watcher.masteries.by_summoner(my_region, me['id'])
#     print(my_mastery_pages)
#
# # lets see if i got diamond yet (i probably didnt)
#     my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])
#     print(my_ranked_stats)
#
# # Lets some champions
#     static_champ_list = watcher.static_data.champions(my_region)
#     print(static_champ_list)
#
#     match_list=watcher.match.matchlist_by_account_recent(my_region,me['accountId'])
#     print(match_list)
#
# # Error checking requires importing HTTPError from requests
#
#     from requests import HTTPError
#
# # For Riot's API, the 404 status code indicates that the requested data wasn't found and
# # should be expected to occur in normal operation, as in the case of a an
# # invalid summoner name, match ID, etc.
# #
# # The 429 status code indicates that the user has sent too many requests
# # in a given amount of time ("rate limiting").
#
#     try:
#         response = watcher.summoner.by_name(my_region, 'this_is_probably_not_anyones_summoner_name')
#     except HTTPError as err:
#         if err.response.status_code == 429:
#             print('We should retry in {} seconds.'.format(e.headers['Retry-After']))
#             print('this retry-after is handled by default by the RiotWatcher library')
#             print('future requests wait until the retry-after time passes')
#         elif err.response.status_code == 404:
#             print('Summoner with that ridiculous name not found.')
#         else:
#             raise

