#!/usr/bin/python3
"""a recursive function that returns a list containing the
    titles of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):

    headers = {"User-Agent": "AllHotposts/1.0"}
    params = {"after": after}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        response_data = response.json()
        data_list = response_data["data"]["children"]
        for hot_posts in data_list:
            hot_list.append(hot_posts["data"]["title"])
        if response_data["data"]["after"] is not None:
            after = response_data["data"]["after"]
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
