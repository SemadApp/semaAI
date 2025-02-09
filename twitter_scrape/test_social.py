import requests
import os
from dotenv import load_dotenv
import pandas as pd

# # Load environment variables from .env file
# load_dotenv()

# # Bearer Token for authentication
# bearer_token = os.getenv("SOCIAL_API")

# # Headers with Bearer Token
# headers = {
#     "Authorization": f"Bearer {bearer_token}",
#     "Content-Type": "application/json"
# }

# # URL for the tweet thread
# tweet_id = "1883532536061759642"
# url = f"https://api.socialdata.tools/twitter/tweets/{tweet_id}"



# # Make the GET request
# response = requests.get(url, headers=headers)

# # Check the response
# if response.status_code == 200:
#     data = response.json()
#     print(data)
# else:
#     print(f"Error: {response.status_code}")
#     print(response.text)  # Print the error message for debugging



# Social Data API credentials
API_KEY = os.getenv("SOCIAL_API")  # Replace with your actual API key
TWEET_ID = "1883532536061759642"  # Replace with the tweet ID you want to analyze

# Social Data API endpoints
BASE_URL = "https://api.socialdata.tools/twitter/tweets/{TWEET_ID}"  # Replace with the actual API base URL
LIKES_URL = f"https://api.socialdata.tools/twitter/tweets/{TWEET_ID}/likes"
RETWEETS_URL = f"{BASE_URL}/retweets"
REPLIES_URL = f"{BASE_URL}/replies"

# Headers for authentication
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Function to fetch data from Social Data API
def fetch_data(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 401:
        raise Exception("Unauthorized: Check your API key.")
    elif response.status_code == 429:
        raise Exception("Rate limit exceeded. Try again later.")
    elif response.status_code != 200:
        raise Exception(f"Request returned an error: {response.status_code} {response.text}")
    return response.json()

try:
    # Fetch users who liked the tweet

    likes_data = fetch_data(LIKES_URL)
    likes_users = likes_data.get("data", [])
    print(likes_data)

    # # Fetch users who retweeted the tweet
    # retweets_data = fetch_data(RETWEETS_URL)
    # retweets_users = retweets_data.get("data", [])
    # print(f"Retweets: {len(retweets_users)}")

    # # Fetch replies to the tweet
    # replies_data = fetch_data(REPLIES_URL)
    # replies_users = replies_data.get("data", [])
    # print(f"Replies: {len(replies_users)}")

    # # Combine all engagement data
    # engagements = []
    # for user in likes_users:
    #     engagements.append({"user_id": user["id"], "username": user.get("username", "N/A"), "engagement_type": "like"})
    # for user in retweets_users:
    #     engagements.append({"user_id": user["id"], "username": user.get("username", "N/A"), "engagement_type": "retweet"})
    # for user in replies_users:
    #     engagements.append({"user_id": user["id"], "username": user.get("username", "N/A"), "engagement_type": "reply"})

    # # Save data to CSV
    # df = pd.DataFrame(engagements)
    # df.to_csv("tweet_engagements.csv", index=False)
    # print("Data saved to tweet_engagements.csv")

except Exception as e:
    print(f"An error occurred: {e}")