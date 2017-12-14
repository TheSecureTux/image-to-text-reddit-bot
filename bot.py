#!/usr/bin/python
import os
import re
import sys
import wget
import praw
import requests
from StringIO import StringIO
from google.cloud import vision
from google.cloud.vision import types



# Function to post the text (ocr_data) to reddit as a comment. Autotext added.
def post_comment(ocr_data):
    submission.reply(ocr_data + "\n\n __________________________________________ \n\n This is a bot still in beta, but the OCR has been improved (hopefully). Please direct all hate and complaints to my master /u/audscias , thank you, puny humans\n ^^r/image_to_text_beta")


# Call to OCR API
def detect_text_uri(uri):
    """Detects text in the file located in Google Cloud Storage or on the Web.
    """
    client = vision.ImageAnnotatorClient()
    image = types.Image()
    image.source.image_uri = uri

    response = client.text_detection(image=image)
    texts = response.text_annotations

    for text in texts:
        return text.description


# Declare the bot instance it's going to be pick the details for on praw.ini
reddit = praw.Reddit('bot1')

# Declare in which subreddit are we going to work
subreddit = reddit.subreddit("4chan")


# Loop through the subreddit submissions and actually do the magic
for submission in subreddit.hot(limit=10):
    # Let's check if have a list of posts we already commented
    if not os.path.isfile("posts_replied_to.txt"):
        posts_replied_to = []
    else:
        # Open the list and read one by one. Also get the domain where it's posted
        with open("posts_replied_to.txt", "r") as f:
            submissiondomain = submission.domain
       	    posts_replied_to = f.read()
       	    posts_replied_to = posts_replied_to.split("\n")
            posts_replied_to = list(filter(None, posts_replied_to))
            # Check if domain is i.redd.it and not already commented on:
            if submissiondomain == 'i.redd.it' and submission.id not in posts_replied_to:
                post_content =  detect_text_uri(submission.url)
                print post_content
                # Post comment on reddit
                post_comment(post_content)
                # Add post id to the list
                posts_replied_to.append(submission.id)
                with open("posts_replied_to.txt", "w") as f:
                    for post_id in posts_replied_to:
                        f.write(post_id + "\n")
