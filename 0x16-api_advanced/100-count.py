#!/usr/bin/python3
"""
Script to count words in all hot posts of a given Reddit subreddit
"""

import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Recursively queries the Reddit API and counts occurrences of keywords
    in hot article titles.

    Args:
        subreddit: A string representing the subreddit to search.
        word_list: A list of strings containing keywords to count.
        after: A string representing the 'after' parameter for pagination.
        word_count: A dictionary to store word counts (default empty).

    Returns:
        A dictionary containing counts of keywords in hot article titles.
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'MyBot/1.0'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json().get('data', {}).get('children', [])
        if data:
            for post in data:
                title = post['data']['title'].lower()
                for word in word_list:
                    word = word.lower()
                    if ' ' + word + ' ' in title:
                        word_count[word] = word_count.get(word, 0) + \
                                           title.count(' ' + word + ' ')
        after = response.json().get('data', {}).get('after')
        if after is not None:
            count_words(subreddit, word_list, after, word_count)
    return word_count


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming "
              "'python java javascript'".format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        word_list = sys.argv[2].split()
        word_count = count_words(subreddit, word_list)
        if word_count:
            sorted_counts = sorted(word_count.items(),
                                   key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print("{}: {}".format(word, count))
