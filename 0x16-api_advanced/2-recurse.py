#!/usr/bin/python3
"""
This module provides a recursive function to query the Reddit API and return
a list containing the titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Queries the Reddit API recursively and returns a list containing the
    titles of all hot articles for a given subreddit. If no results are
    found, returns None.
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'MyAPIProject/0.0.1'}
    params = {'after': after, 'limit': 100}

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
        )
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                hot_list.append(post['data']['title'])
            after = data['data']['after']
            if after is not None:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list if hot_list else None
        else:
            return None
    except requests.RequestException:
        return None


# Example usage
if __name__ == "__main__":
    subreddit = input("Enter the name of the subreddit: ")
    titles = recurse(subreddit)
    if titles:
        print("Titles of all hot articles:")
        for title in titles:
            print(title)
    else:
        print(None)
