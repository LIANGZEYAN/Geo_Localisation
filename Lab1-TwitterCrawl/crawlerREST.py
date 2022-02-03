import tweepy
import json

import sys

# You need to replace these with your own values that you get after creating an app on Twitter's developer portal.
consumer_key = "E xJ"
consumer_secret ="eRpAtSZ E"
access_token ="267112 D"
access_token_secret ="UQ 4y"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret )
auth.set_access_token(access_token, access_token_secret)

class StreamListener(tweepy.StreamListener):
  #This is a class provided by tweepy to access the Twitter Streaming API.
    def on_connect(self):
        # Called initially to connect to the Streaming API
        print("You are now connected to the streaming API.")

    def on_error(self, status_code):
        # On error - if an error occurs, display the error / status code
        print('An Error has occured: ' + repr(status_code))
        return False

    def on_data(self, data):
        # This is the meat of the script...it connects to your mongoDB and stores the tweet
        print("data holder")
        # try:
        # print(data)
        #
        # except Exception as e:
        #     print(e)


#Set up the listener. The 'wait_on_rate_limit=True' is needed to help with Twitter API rate limiting.
listener = StreamListener(api=tweepy.API(wait_on_rate_limit=True))
streamer = tweepy.Stream(auth=auth, listener=listener)
# streamer.sample(languages = ['en'])
#
Loc_UK = [-10.392627, 49.681847, 1.055039, 61.122019] # UK and Ireland
Words_UK =["Boris", "Prime Minister", "Tories", "UK", "London", "England", "Manchester", "Sheffield", "York", "Southampton", \
 "Wales", "Cardiff", "Swansea" ,"Banff", "Bristol", "Oxford", "Birmingham" ,"Scotland", "Glasgow", "Edinburgh", "Dundee", "Aberdeen", "Highlands" \
"Inverness", "Perth", "St Andrews", "Dumfries", "Ayr" \
"Ireland", "Dublin", "Cork", "Limerick", "Galway", "Belfast"," Derry", "Armagh" \
"BoJo", "Labour", "Liberal Democrats", "SNP", "Conservatives", "First Minister", "Surgeon", "Chancelor" \
"Boris Johnson", "BoJo", "Keith Stramer"]
# #
# # print("Tracking: " + str(Words_UK))
# streamer.filter(locations= Loc_UK, track = Words_UK, languages = ['en'], is_async=True) #locations= Loc_UK, track = Words_UK,
# #

api = tweepy.API(auth)
Place =  'London'
Lat   =  '51.450798'
Long  =  '-0.137842'
geoTerm=Lat+','+Long+','+'10km'
#

last_id =  None
counter =0
sinceID = None

results = True
results = api.search(geocode=geoTerm, count=100, lang="en", tweet_mode='extended', max_id=last_id)
print(results)
# sys.exit(1)
#
# while results:
#     # print(geoTerm)
#
#     if (counter < 180 ):
#         try:
#             results = api.search(geocode=geoTerm, count=100, lang="en", tweet_mode='extended', max_id=last_id) #, since_id = sinceID)
#             print(results)
#         except Exception as e:
#             print(e)
#         counter += 1
#     else:
#         #  the following let the crawler to sleep for 15 minutes; to meet the Tiwtter 15 minute restriction
#         time.sleep(15*60)
#
