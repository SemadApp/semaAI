import tweepy
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Twitter API credentials
API_KEY = os.getenv("TWITTER_API_KEY")
API_SECRET = os.getenv("TWITTER_API_SECRET")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")

# Authenticate with Twitter API v1.1
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# Username of the user (Suhail Kakar's Twitter handle)
username = "SuhailKakar"  # Change to Suhail Kakar's Twitter handle

# Fetch tweets by Suhail Kakar (you can increase count if needed)
tweets = api.user_timeline(screen_name=username, count=1, tweet_mode="extended")

# Filter and print threads
for tweet in tweets:
    # Checking if the tweet is part of a thread
    if hasattr(tweet, 'in_reply_to_status_id_str') and tweet.in_reply_to_status_id_str is not None:
        print(f"Thread tweet from {username}: {tweet.full_text}")
        print(f"Likes: {tweet.favorite_count}, Retweets: {tweet.retweet_count}")
        print("-" * 50)
    else:
        print(f"Single tweet from {username}: {tweet.full_text}")
        print(f"Likes: {tweet.favorite_count}, Retweets: {tweet.retweet_count}")
        print("-" * 50)
