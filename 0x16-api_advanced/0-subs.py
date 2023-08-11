#!/usr/bin/python3
""" returns the number of subscribers for a given subreddit"""
import requests


def number_of_subscribers(subreddit):

    headers = {"User-Agent": "SubscribersCount/1.0"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        response_data = response.json()
        subscribers = response_data["data"]["subscribers"]
        return subscribers
    else:
        return 0
