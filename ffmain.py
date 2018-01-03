import urllib
import bs4
import re
import redditTest
import praw
import hashlib

from urllib.request import urlopen
from bs4 import BeautifulSoup

ffxivLodeNewsUrl = "https://na.finalfantasyxiv.com/lodestone/news/"

soup = BeautifulSoup(urlopen(ffxivLodeNewsUrl), "html5lib")
soup3= (soup.select('.news__list--topics'))

reddit = praw.Reddit(client_id='xxxxxx',
                     client_secret='xxxxxx',
                     user_agent='sgBot/0.01 by 0xFF4501',
                     username='xxxxxx',
                     password='xxxxxx')

# soup1= (soup.select('.news__list--topics')[0])
#
# def testtitle():
#     return (soup1.find_all('p')[0].text)
# def testdesc():
#     return (soup1.find_all('p')[2].text)
# def testthing():
#     articleLink = ("https://na.finalfantasyxiv.com" + (soup.find("a", {"href":re.compile("/lodestone/topics/detail/")})['href']))
#     return(articleLink)
# print (articleLink)

listSubTitlesMD5 = []



def computeMD5hash(my_string):
    m = hashlib.md5()
    m.update(my_string.encode('utf-8'))
    return m.hexdigest()

def difmain(title,article,url):
    for submission in reddit.subreddit('sgBotSub').new(limit=20):
        listSubTitlesMD5.append(computeMD5hash(submission.title))
difmain(0,0,0)
print (listSubTitlesMD5)

for soup2 in soup3[::-1]:
    print ("==========================")
    print (soup2.find_all('p')[0].text)
    artTitle = (soup2.find_all('p')[0].text)
    artTitle = artTitle.strip()

    print (soup2.find("img", {"src":re.compile("img.finalfantasyxiv.com/t/")})['src'])



    print ("https://na.finalfantasyxiv.com" + (soup2.find("a", {"href":re.compile("/lodestone/topics/detail/")})['href']))
    artUrl = ("https://na.finalfantasyxiv.com" + (soup2.find("a", {"href":re.compile("/lodestone/topics/detail/")})['href']))


    if len((soup2.find_all('p')[1].text)) > 10:
        print (soup2.find_all('p')[1].text)
        artArt = (soup2.find_all('p')[1].text)
    else:
        print (soup2.find_all('p')[2].text)
        artArt = (soup2.find_all('p')[2].text)

    redditTest.main(artTitle, artArt,artUrl)
