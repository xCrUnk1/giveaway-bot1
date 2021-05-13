from tweepy import StreamListener
from tweepy import Stream
import time
from discord_webhook import DiscordWebhook, DiscordEmbed
import tweepy

API_KEY = 'ADG0JOYxosKvUZzbC8D5P87ss'
API_SECRET_KEY = '9MxGEfqGRaUyULdgNp21pEOLrPvTCU1WmSo7QxUEqcvLbLieSA'
ACCESS_TOKEN = '1289620640291594242-90XrOaUZoz95nZXBSE1n2BcnaXOMHc'
ACCESS_TOKEN_SECRET = 'vh6Sy4Jg7SmuP4mnNLyGiSx2Ut9CcwBqwedfuIVW8wzzA'
twitter_id = '1289620640291594242'
twitter_id_tartarus = '1222179687188832256'

Tweets = []


auth = tweepy.OAuthHandler('BKROSah4DvttUZxKPhah8mYGR', '5v82CvCwlYc738eCAbJcQW94R8xCABeUj01fXKu8w4PGDlPB7t')
auth.set_access_token('1289620640291594242-FeKnc3oOpGOr05z2XZtZyVnwvjgkqI', 'cpNXgP6MoigF9IxFTxY3h1UHKlwZGjLMxjQhQztRDzhtH')
api = tweepy.API(auth, wait_on_rate_limit=True)

usernames = None
profile_images = None
follower_numbers = None
bio_users = None
bio_urls = None
tweet_contents = None
tweet_urls = None

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.user.screen_name + ' tweetet: ' + status.text + '\n' + 'Follower Count' + str(status.user.followers_count))
        print('Bio: ' + str(status.user.description))
        print(status.user.profile_image_url)

        usernames = status.user.screen_name
        tweet_contents = status.text
        follower_numbers = str(status.user.followers_count)
        tweet_urls = 'https://twitter.com/xCrUnk3/status/' + str(status.id)
        bio_users = str(status.user.description)
        webhook = DiscordWebhook(url='https://discord.com/api/webhooks/790197755632418846/PgpMHTX_KOFVwczgsF6lInniJBhyjL3lU4oT-9nUicUoPdumvEI50CZbEIPcL0m8cPVZ')
        embed = DiscordEmbed(title=usernames, description=tweet_contents, color=242424)
        webhook.add_embed(embed)
        response = webhook.execute()


def streamtweets():
    xcrunk_Listener = MyStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=xcrunk_Listener)
    myStream.filter(follow=[twitter_id])


streamtweets()
