import urllib
import bs4
import re
import praw
import hashlib
import requests
import requests.auth
import time

from urllib.request import urlopen
from bs4 import BeautifulSoup

# Setting up data for the reddit api
reddit = praw.Reddit(client_id='CXRzSmeVw_lx0g',
                     client_secret='xfsMu3CiHNdGRmmAMnpoQZ5ROT0',
                     user_agent='sgBot/0.01 by 0xFF4501',
                     username='0xFF4501',
                     password='p4ssw0rd')

# FFXIV news website
ffxivLodeNewsUrl = "https://na.finalfantasyxiv.com/lodestone/news/"
# Opening and storing the site to soup
soup = BeautifulSoup(urlopen(ffxivLodeNewsUrl), "html5lib")
# Selecting the requierd articles using their CSS
soup3= (soup.select('.news__list--topics'))

# Creating a list to store MD5 hashes of 20 most recent post titles
listSubTitlesMD5 = []

# Hash function
def computeMD5hash(string_in):
    m = hashlib.md5()
    m.update(string_in.encode('utf-8'))
    return m.hexdigest()

# Hashing 20 most recent posted titles
def hashSubTitles():
    for submission in reddit.subreddit('sgBotSub').new(limit=20):
        listSubTitlesMD5.append(computeMD5hash(submission.title.strip()))
# Actually calling the function
hashSubTitles()
print (listSubTitlesMD5)


def process_submission(submission, title, article):
    if computeMD5hash(submission.title).strip() == computeMD5hash(title.strip()):
        reply_text = article
        submission.reply(reply_text)
        return
    else:
        return


def checkAndPost():
    for soup2 in soup3[::-1]:
        artTitle = (soup2.find_all('p')[0].text)
        artTitle = artTitle.strip()
        artUrl = ("https://na.finalfantasyxiv.com" + (soup2.find("a", {"href":re.compile("/lodestone/topics/detail/")})['href']))
        if len((soup2.find_all('p')[1].text)) > 10:
            print (soup2.find_all('p')[1].text)
            artArt = (soup2.find_all('p')[1].text)
        else:
            print (soup2.find_all('p')[2].text)
            artArt = (soup2.find_all('p')[2].text)
        if computeMD5hash(artTitle) in listSubTitlesMD5:
            pass
        else:
            reddit.subreddit('sgBotSub').submit(artTitle, url=artUrl)
            hashSubTitles()
            for submission in reddit.subreddit('sgBotSub').new(limit=20):
                process_submission(submission, artTitle, artArt)
                break
    time.sleep(300)

while True:
    checkAndPost()

