# image-to-text-reddit-bot
Reddit bot to transcribe text from images to a post using Google Cloud Vision API

# How to use it

Just download the bot.py and the posts_replied_to.txt	file on the same folder and run it with

    python bot.py

You will see on stdout the text that is going to be posted.

You need to create a praw.ini file to pass the PRAW api the credentials for your bot to be able to post the results on reddit. Please refer to the praw documentation for more info on that:

https://praw.readthedocs.io/en/latest/

