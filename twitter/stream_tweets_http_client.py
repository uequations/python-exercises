#!/bin/python3

import sys
import requests
import requests_oauthlib
import json

# Replace the values below with yours
ACCESS_TOKEN = 'MY_ACCESS_TOKEN'
ACCESS_SECRET = 'MY_ACCESS_SECRET'
CONSUMER_KEY = 'MY_CONSUMER_KEY'
CONSUMER_SECRET = 'MY_CONSUMER_SECRET'

# query params
MY_LOCATION = '-130,-20,100,50'

my_auth = requests_oauthlib.OAuth1(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

def get_tweets():
    url = 'https://stream.twitter.com/1.1/statuses/filter.json'
    query_data = [('language', 'en'), ('locations', MY_LOCATION), ('track', '#')]
    query_url = url + '?' + '&'.join([str(t[0]) + '=' + str(t[1]) for t in query_data])
    response = requests.get(query_url, auth=my_auth, stream=True)
    print(query_url, response)
    return response

def read_tweets_in_response(http_resp):
    for line in http_resp.iter_lines():
        try:
            full_tweet = json.loads(line)
            tweet_text = full_tweet['text']
            print("Tweet Text: " + tweet_text)
        except:
            e = sys.exc_info()[0]
            print("Error: %s" % e)

if __name__ == '__main__':
    read_tweets_in_response(get_tweets())
