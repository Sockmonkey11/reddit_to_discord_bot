import praw
import schedule
import requests
import time
import os 
try:
    import config
except ImportError:
    config = None

username = os.getenv("REDDIT_USERNAME") or (config.username if config else None)
password = os.getenv("REDDIT_PASSWORD") or (config.password if config else None)
client_id = os.getenv("REDDIT_CLIENT_ID") or (config.client_id if config else None)
client_secret = os.getenv("REDDIT_CLIENT_SECRET") or (config.client_secret if config else None)
webhook = os.getenv("DISCORD_WEBHOOK") or (config.DISCHORD_WEBHOOK_URL if config else None)

DISCHORD_WEBHOOK_URL = webhook

def bot_login():
    print ("Logging in...")
    r = praw.Reddit(username = username,
                password = password,
                client_id = client_id,
                client_secret = client_secret,
                user_agent = "Cat_test by u/Cat_test v1.0")
    print ("Logged in!")
    return r

def run_bot(r):
    title_list = []
    list_number = 0
    niche_subreddit = r.subreddit('wallstreetbets') 
    for submission in niche_subreddit.hot(limit=10):
        title_list.append(submission.title + " " + submission.url + "\n")
    print("10 hottest post titles in r/wallstreetbets:")
    for title in title_list:
        requests.post(DISCHORD_WEBHOOK_URL, json={"content": title})
        list_number += 1
        print(f"{list_number}. {title}")
        

r = bot_login()
run_bot(r)





# schedule.every().day.at("10:35").do(run_bot, r)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
# This code logs into Reddit, retrieves the 10 hottest posts from r/wallstreetbets, and sends their titles to a Discord webhook.

        
    
    
    