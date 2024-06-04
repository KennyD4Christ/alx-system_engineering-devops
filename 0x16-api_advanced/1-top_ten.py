#!/usr/bin/python3
"""
This module provides a function to query the Reddit API and print the
titles of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot
    posts listed for a given subreddit. If not a valid subreddit,
    prints None.
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'MyAPIProject/0.0.1'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                print(post['data']['title'])
        else:
            print(None)
    except requests.RequestException:
        print(None)


# Example usage
if __name__ == "__main__":
    subreddit = input("Enter the name of the subreddit: ")
    top_ten(subreddit)
