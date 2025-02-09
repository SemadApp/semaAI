import tweepy
import os
from dotenv import load_dotenv
from pymongo import MongoClient
import time
from datetime import datetime

# Load environment variables
load_dotenv()

# Twitter API credentials
API_KEY = os.getenv("TWITTER_API_KEY")
API_SECRET = os.getenv("TWITTER_API_SECRET")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")

# MongoDB URI
MONGO_URI = os.getenv("MONGO_URI")

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client["twitter_db"]
collection = db["AI_mentions"]

# Authenticate with Twitter API v1.1
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

def fetch_and_store_mentions():
    query = "#AI -filter:retweets"  # Search for mentions of @semaAI excluding retweets
    mentions = api.search_tweets(q=query, count=10, tweet_mode="extended")

    if mentions:
        for tweet in mentions:
            tweet_data = {
                "user_id": tweet.user.id_str,
                "tweet_id": tweet.id_str,
                "username": tweet.user.screen_name,
                "content": tweet.full_text,
                "likes": tweet.favorite_count,
                "retweets": tweet.retweet_count,
                "created_at": tweet.created_at,
                "timestamp": datetime.utcnow()
            }
            # Insert tweet data into MongoDB
            collection.insert_one(tweet_data)
            print(f"Saved Tweet ID: {tweet.id_str}")

    else:
        print("No new mentions found.")

# Run the script every 10 seconds
while True:
    fetch_and_store_mentions()
    print("Waiting 10 seconds before checking again...")
    time.sleep(10)
