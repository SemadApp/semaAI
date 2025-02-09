import requests
import os
from dotenv import load_dotenv


BEARER_TOKEN = os.getenv("BEARER_TOKEN")
TEST_URL = "https://api.twitter.com/2/tweets/20"  # Example tweet ID

headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}",
    "User-Agent": "v2TweetLookupPython"
}

response = requests.get(TEST_URL, headers=headers)
print(response.status_code)
print(response.json())