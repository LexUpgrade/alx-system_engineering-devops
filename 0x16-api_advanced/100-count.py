#!/usr/bin/python3
"""Defines a function <count_words>."""
import requests


def count_words(subreddit, word_list, instances={}, after="", count=0):
    """Prints counts of given words found in a hot posts of a given sudreddit.

    Args:
        subrredit (str): The subreddit to search.
        word_list (list): The list of words to search for in post tiltes.
        instances (dict): key/value pairs of words/counts.
        after (str): The parameter for the next page of the API results.
        count (int): The parameter of results matched thus far.
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
    try:
        if response.status_code == 404:
            raise Exception
        data = response.json()
    except Exception:
        print("")
        return

    data = data.get('data')
    after = data.get('after')
    count += data.get('dist')
    for datum in data.get('children'):
        title = datum.get('data').get('title').lower().split()
        for word in word_list:
            if word.lower() in title:
                times = len([t for t in title if t == word.lower()])
                if instances.get(word) is None:
                    instances[word] = times
                else:
                    instances[word] += times

    if after is None:
        if len(instances) == 0:
            print("")
            return
        instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
        [print("{}: {}".format(k, v)) for k, v in instances]
    else:
        count_words(subreddit, word_list, instances, after, count)
