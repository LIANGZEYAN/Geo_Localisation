import tweepy
import json

from pymongo import MongoClient


# You need to replace these with your own values that you get after creating an app on Twitter's developer portal.
consumer_key = "EiGyOzensI9MOwuti2kVWN4xJ"
consumer_secret ="eRpAtSZtbqsX1GfimeuGhr5OWIfi3KLOZdP0Is1PeL2RaTcJ0E"
access_token ="26711278-yoA5Xi0JX3tmZubSvLK2MTDZly6PXJL3NWikJIHpD"
access_token_secret ="UQn1J5t7zUJdxAdSu3Z0nfdiZM7Fk6hfHYkVMqvXOpk4y"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret )
auth.set_access_token(access_token, access_token_secret)

client = MongoClient('127.0.0.1',27017) #is assigned local port
db = client["TwitterDump"]
collection =db['tweetCollection']

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
        #This is the meat of the script...it connects to your mongoDB and stores the tweet
        #print(data)
        # tweetJson = json.loads(data)
        # collection.insert_one(tweetJson)
        try:
            tweetJson = json.loads(data)
            # print(tweetJson)
            collection.insert_one(tweetJson)

        except Exception as e:
            print(e)


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
streamer.filter(locations= Loc_UK, track = Words_UK, languages = ['en'], is_async=True) #locations= Loc_UK, track = Words_UK,
# #
