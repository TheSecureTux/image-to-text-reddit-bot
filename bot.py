#!/usr/bin/python
import sys
import wget
import praw
import pytesseract
import requests
from PIL import Image
from PIL import ImageFilter
from StringIO import StringIO

def process_image(url):
    image = _get_image(url)
    image.filter(ImageFilter.SHARPEN)
    return pytesseract.image_to_string(image)


def _get_image(url):
    return Image.open(StringIO(requests.get(url).content))




reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("ProgrammerHumor")

for submission in subreddit.hot(limit=10):
    submissiondomain = submission.domain
    if submissiondomain == 'i.redd.it':
        print("Domain: ", submissiondomain)
        print("Title", submission.title)
        print("URL: ", submission.url)
	image_data= _get_image(submission.url)


	sys.stdout.write("The raw output from tesseract with no processing is:\n\n")
    	sys.stdout.write("-----------------BEGIN-----------------\n")
    	sys.stdout.write(pytesseract.image_to_string(image_data) + "\n")
    	sys.stdout.write("------------------END------------------\n")	 


 
