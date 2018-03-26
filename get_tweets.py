from twitterscraper import query_tweets
import datetime as dt

if __name__ == '__main__':
    # print the retrieved tweets to the screen:
    for tweet in query_tweets("@UHC", begindate= dt.date(2017,1,1), enddate=dt.date(2017,2,1)):
        print(tweet.id)