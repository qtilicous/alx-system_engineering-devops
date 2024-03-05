#!/usr/bin/python3
"""
A function that queries the Reddit API
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit.

    Args:
        subreddit: A string representing the subreddit to query.

    Returns:
        The number of subscribers for the given subreddit, or 0 if the
        subreddit is invalid.
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': '0x16.API.advanced/1.0 (by /u/qtilicousbbz)'}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return 0
    else:
        data = response.json().get('data')
        if data:
            return data.get('subscribers', 0)
        else:
            return 0


if __name__ == '__main__':
    print(number_of_subscribers('programming'))
