#!/usr/bin/python
import os
import re
import pdb
import sys
import wget
import praw
import pytesseract
import requests
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
from StringIO import StringIO


# Get the content of the image from the URL linked
def _get_image(url):
    return Image.open(StringIO(requests.get(url).content))

# Modify the image to improve chances of correct recognition
def process_image(url):
    image = _get_image(url)
    step1 = image.convert('L')
    step2 = step1.filter(ImageFilter.SHARPEN).filter(ImageFilter.DETAIL)
    return pytesseract.image_to_string(step2)

# Output the text to stdout, useful for debugging
def console_output(ocr_data):
    print("Domain: ", submissiondomain)
    print("Title", submission.title)
    print("URL: ", submission.url)
    sys.stdout.write("The raw output from tesseract OCR for this image is:\n\n")
    sys.stdout.write("-----------------BEGIN-----------------\n")
    sys.stdout.write(ocr_data)
    sys.stdout.write("\n")
    sys.stdout.write("------------------END------------------\n")

# Function to post the text (ocr_data) to reddit as a comment. Autotext added.
def post_comment(ocr_data):
    submission.reply(ocr_data + "\n\n __________________________________________ \n\n This is a bot in early beta. Please direct all hate and complaints to my master /u/audscias , thank you, puny humans\n ^^r/image_to_text_beta")


# Declare the bot instance it's going to be pick the details for on praw.ini
reddit = praw.Reddit('bot1')

# Declare in which subreddit are we going to work
subreddit = reddit.subreddit("linuxmasterrace")


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
                # Let's process the image text
                ocr_data = process_image(submission.url)
                # Show results on stdout
                console_output(ocr_data)
                # Post comment on reddit
                post_comment(ocr_data)
                # Add post id to the list
                posts_replied_to.append(submission.id)
                with open("posts_replied_to.txt", "w") as f:
                    for post_id in posts_replied_to:
                        f.write(post_id + "\n")
