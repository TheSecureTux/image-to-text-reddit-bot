#!/usr/bin/python
import praw
import wget

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("ProgrammerHumor")

for submission in subreddit.hot(limit=10):
    submissiondomain = submission.domain
    if submissiondomain == 'i.redd.it':
        print("Domain: ", submissiondomain)
        print("Title", submission.title)
        print("URL: ", submission.url)
        wget.download(submission.url)
        
