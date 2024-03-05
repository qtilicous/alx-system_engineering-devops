#!/usr/bin/python3
"""
2-recurse
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit.

    Args:
        subreddit: A string representing the subreddit to search.
        hot_list: A list containing the titles of hot articles (default empty).
        after: A string representing the 'after' parameter for pagination.

    Returns:
        A list containing the titles of all hot articles,
        or None if no results are found.
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'MyBot/1.0'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json().get('data', {}).get('children', [])
        if data:
            for post in data:
                hot_list.append(post['data']['title'])
            after = response.json().get('data', {}).get('after')
            if after is not None:
                recurse(subreddit, hot_list, after)
            return hot_list
        else:
            return None
    else:
        return None


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")
