#!/usr/bin/python3
"""
A recursive function that querries reddit API for total number of subsribers
"""
import requests


def number_of_subscribers(subreddit):

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
            'User-agent': 'Mozilla/5.0'
            }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    res = response.json()
    if 'data' not in res:
        return 0
    if 'subscribers' not in res.get('data'):
        return 0
    return response.json()['data']['subscribers']
