#!/usr/bin/python3
"""
1-top_ten
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.

    Args:
        subreddit: A string representing the subreddit to search.

    Prints:
        The titles of the first 10 hot posts for the given subreddit,
        or 'None' if the subreddit is invalid.
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': '0x16.API.advanced/1.0 (by /u/qtilicousbbz)'}
    params = {'limit': 10}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        print(None)
    else:
        data = response.json().get('data', {}).get('children', [])
        if data:
            for post in data:
                print(post['data']['title'])
        else:
            print(None)


if __name__ == '__main__':
    top_ten('programming')
