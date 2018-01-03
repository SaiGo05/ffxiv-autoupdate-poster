# Your username is: xxxxxx
# Your password is: xxxxxx
# Your app's client ID is: xxxxxx
# Your app's client secret is: xxxxxx
# {'access_token': 'xxxxxx', 'token_type': 'bearer', 'expires_in': 3600, 'scope': '*'}
import requests
import requests.auth
import praw
import hashlib
reddit = praw.Reddit(client_id='xxxxxx',
                     client_secret='xxxxxx',
                     user_agent='sgBot/0.01 by 0xFF4501',
                     username='xxxxxx',
                     password='xxxxxx')

# client_auth = requests.auth.HTTPBasicAuth('xxxxxx', 'xxxxxx')
# post_data = {"grant_type": "password", "username":"xxxxxx", "password":"xxxxxx"}
# headers = {"User-Agent":"sgBot/0.01 by 0xFF4501"}
# response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
# response.json()
# headers = {"Authorization": "bearer xxxxxx", "User-Agent":"sgBot/0.01 by 0xFF4501"}
# response = requests.get("https://oauth.reddit.com/api/v1/me", headers=headers)
# response.json()



def main(title,article,url):
    reddit.subreddit('sgBotSub').submit(title, url=url)
    subreddit = reddit.subreddit('sgBotSub')
    for submission in reddit.subreddit('sgBotSub').new(limit=20):
        process_submission(submission, title, article)
        break


def process_submission(submission, title, article):
    print (submission.title)
    print (computeMD5hash(submission.title))
    print (title)
    print(computeMD5hash(title))
    if computeMD5hash((submission.title).strip()) == computeMD5hash(title.strip()):
        reply_text = article
        submission.reply(reply_text)
        return
    else:
        return


def computeMD5hash(my_string):
    m = hashlib.md5()
    m.update(my_string.encode('utf-8'))
    return m.hexdigest()
