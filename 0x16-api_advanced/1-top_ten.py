#!/usr/bin/python3
""" prints the titles of the first 10 hot posts listed for a given subreddit"""
import requests


def top_ten(subreddit):

    headers = {"User-Agent": "TopHotposts/1.0"}
    params = {"limit": 10}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        response_data = response.json()
        data_list = response_data["data"]["children"]
        for hot_posts in data_list:
            post_title = hot_posts["data"]["title"]
            print(post_title)
    else:
        print(None)
