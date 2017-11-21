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



def _get_image(url):
    return Image.open(StringIO(requests.get(url).content))

def process_image(url):
    image = _get_image(url)
    image.filter(ImageFilter.SHARPEN)
    image.filter(ImageFilter.SHARPEN)
    return pytesseract.image_to_string(image)


def console_output(ocr_data):
    sys.stdout.write("The raw output from tesseract OCR for this image is:\n\n")
    sys.stdout.write("-----------------BEGIN-----------------\n")
    sys.stdout.write(ocr_data)
    sys.stdout.write("\n")
    sys.stdout.write("------------------END------------------\n")

def post_comment(ocr_data):
    submission.reply(ocr_data + "\n\n __________________________________________ \n\n This is a bot in early beta. Please direct all hate and complaints to my master /u/audscias , thank you, puny humans\n ^^r/image_to_text_beta")



reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("image_to_text_beta")

for submission in subreddit.hot(limit=10):
    submissiondomain = submission.domain
    if not os.path.isfile("posts_replied_to.txt"):
        posts_replied_to = []
    else:
        with open("posts_replied_to.txt", "r") as f:
       	    posts_replied_to = f.read()
       	    posts_replied_to = posts_replied_to.split("\n")
            posts_replied_to = list(filter(None, posts_replied_to))
            if submissiondomain == 'i.redd.it' and submission.id not in posts_replied_to:
                print("Domain: ", submissiondomain)
                print("Title", submission.title)
                print("URL: ", submission.url)
                # image_data= _get_image(submission.url)
                # ocr_data= _get_image(image_data)
                ocr_data = process_image(submission.url)
                console_output(ocr_data)
                post_comment(ocr_data)
                posts_replied_to.append(submission.id)
                with open("posts_replied_to.txt", "w") as f:
                    for post_id in posts_replied_to:
                        f.write(post_id + "\n")
