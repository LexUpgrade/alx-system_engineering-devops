#!/usr/bin/python3
"""Defines a function <number_of_subscribers>."""
import requests


def number_of_subscribers(subreddit):
    """Queries a Reddit API and return the number of subscribers of a
    given subreddit.
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': "linux:0x16-api_advanced:v1.0.0 (by u/lex9jar)"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    data = response.json().get('data')
    return data.get('subscribers')
