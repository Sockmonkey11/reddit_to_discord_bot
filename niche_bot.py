import praw
import config
import schedule
import requests
import time
DISCHORD_WEBHOOK_URL = config.DISCHORD_WEBHOOK_URL
def bot_login():
    print ("Logging in...")
    r = praw.Reddit(username = config.username,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
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
# Schedule the bot to run every day at 10:35 AM
schedule.every().day.at("10:35").do(run_bot, r)

while True:
    schedule.run_pending()
    time.sleep(1)
# This code logs into Reddit, retrieves the 10 hottest posts from r/wallstreetbets, and sends their titles to a Discord webhook.

        
    
    
    