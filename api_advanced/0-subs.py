#!/usr/bin/python3
"""
Module to query Reddit API for subscriber count
"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:myredditapp:v1.0.0 (by /u/yourusername)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return response.json().get("data", {}).get("subscribers", 0)
    return 0
