import requests
import praw
import random

reddit = praw.Reddit(client_id='',
                     client_secret='', user_agent='')

#subreddit = input('Input a subreddit >')


def top_post(subreddit):
    links = []
    get_post = reddit.subreddit(f'{subreddit}').top(limit=10)
    for posts in get_post:
        img = posts.url
        body = posts.selftext.strip()
        links.append(img)
    # print(random.choice(links))
    return random.choice(links)


def newPost(subreddit):
    links = []
    subreddit = input('Enter a subreddit to get the 10 newest posts > ')
    get_post = reddit.subreddit(f'{subreddit}').new(limit=10)
    for posts in get_post:
        img = posts.url
        body = posts.selftext.strip()
        links.append(img)


def hotPost(subreddit):
    links = []
    get_post = reddit.subreddit('all').hot(limit=50)
    for posts in get_post:
        img = posts.url
        links.append(img)
        body = posts.selftext.strip()
    return random.choice(links)
