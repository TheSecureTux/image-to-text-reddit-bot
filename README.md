# image-to-text-reddit-bot
Reddit bot to transcribe text from images to a post using Tesseract OCR

- https://github.com/tesseract-ocr/tesseract

The bot uses Tesseract and the wrapper pytesseract in conjunction with praw to scan the most popular posts with images on a subreddit and post the resulting text as a comment.

- pytesseract Github: https://github.com/madmaze/pytesseract
- praw Github: https://github.com/praw-dev/praw

Right now the work focuses on improving the wuality of the results by tuning the image that it's fed to Tesseract with PIL:

- http://www.pythonware.com/products/pil/

In the near future the learning capabilities of Tesseract v.4 will be implemented so it can learn from human transcribers such as these guys, who are doing an awesome and invaluable work:

- https://www.reddit.com/r/TranscribersOfReddit/
