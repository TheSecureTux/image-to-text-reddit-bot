#!/usr/bin/python
import praw
# import pyocr


reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("ProgrammerHumor")

for submission in subreddit.hot(limit=10):
    if reddit.domain('i.redd.it'):
        print("Title: ", submission.title)
        print("Text: ", submission.selftext)
        print("Score: ", submission.score)
        print("---------------------------------\n")
        print("Subdomain", submission.domain)
