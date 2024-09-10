#!/usr/bin/python3
"""Defines a function <top_ten>."""
import requests


def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the first 10
    hot posts listed for the given <subreddit>.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {'User-Agent': "linux:0x16-api_advanced:v1.0.0 (by u/lex9jar)"}
    params = {'limit': 10}

    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print('None')
        return
    data = response.json().get('data')
    [print(datum.get('data').get('title')) for datum in data.get('children')]
