import praw
import config

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
    niche_subreddit = r.subreddit('wallstreetbets') 
    for submission in niche_subreddit.hot(limit=10):
        title_list.append(submission.title + " " + submission.url + "\n")
    print("10 hottest post titles in r/wallstreetbets:")
    for title in title_list:
        print(title)
        

r = bot_login()
run_bot(r)
        
    
    
    