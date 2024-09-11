#!/usr/bin/python3
"""Defines a function <recurse>."""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Queries the Reddit API and returns a list containing the titles of
    all hot articles for a given subreddit. If no results are found for
    the given subreddit, the function returns <None>.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {'User-Agent': "linux:0x16-api_advanced:v1.0.0 (by u/lex9jar)"}
    params = {
            'after': after,
            'count': count,
            'limit': 100
            }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    data = response.json().get('data')
    after = data.get('after')
    count += data.get('dist')
    for datum in data.get('children'):
        hot_list.append(datum.get('data').get('title'))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
