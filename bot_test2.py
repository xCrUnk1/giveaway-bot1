import time
import tweepy
import logging
import random
from os import environ

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

API_KEY = 'API_KEY'
API_SECRET_KEY = 'API_SECRET_KEY'
ACCESS_TOKEN = 'ACCESS_TOKEN'
ACCESS_TOKEN_SECRET = 'ACCESS_TOKEN_SECRET'

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)



def retweet_tweets_with_hashtags(api, need_hashtags):
    mentions = []
    print('___________________')

    if type(need_hashtags) is list:
        search_query = f"{need_hashtags} -filter:retweets"
        tweets = api.search(q=search_query, lang = "en", tweet_mode='extended')
        for tweet in tweets:
            hashtags = [i['text'].lower() for i in tweet.__dict__['entities']['hashtags']]
            text = tweet.__dict__['full_text'].lower()
            print(text)
            #print(hashtags)

            # Scrapen von allen Mentions in dem Beitrag mit den entsprechenden Keywords
            for i in range(len(tweet.__dict__['entities']['user_mentions'])):
                mentions = []
                mentions.append(tweet.__dict__['entities']['user_mentions'][i]['screen_name'])
            print(mentions)
            try:

                need_hashtags = list(need_hashtags)
                print(need_hashtags)
                if need_hashtags[0] in text or need_hashtags[1] in text or need_hashtags[2] in text:
                    print('keyword drin')
                    if tweet.user.id != api.me().id:
                        print('bestanden')

                        tweet.favorite()
                        tweet.retweet()
                        print('retweetet')
                        # Wenn Liste mehr als eine Mention enthält soll er alle mentions folgen!
                        if len(mentions) != 0:
                            api.create_friendship(tweet.user.screen_name)
                            for i in range(len(mentions)):
                                print(mentions[i])
                                api.create_friendship(mentions[i])
                                time.sleep(3)

                        api.update_status('@eddiethewashed ' + '@raju187 ' + '@braindead8270'+ ' ' + '@' + tweet.user.screen_name, tweet.id)
                        logger.info(f"Retweeted tweet from {tweet.user.name}")
                        print('Ende')
                        time.sleep(200)

            except tweepy.TweepError:
                logger.error("Error on retweet", exc_info=True)
    else:
        logger.error("Hashtag search terms needs to be of type list", exc_info=True)
        return




while True:
    retweet_tweets_with_hashtags(api, ['giveaway', 'like', 'retweet'])
    logger.info("Waiting...")
    time.sleep(500)