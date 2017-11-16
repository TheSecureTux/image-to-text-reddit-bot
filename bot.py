#!/usr/bin/python
import praw
import pyocr


reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("programmer_humour")

for submission in subreddit.hot(limit=5):
    if reddit.domaim('imgur.com')
