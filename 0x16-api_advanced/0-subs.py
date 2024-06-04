#!/usr/bin/python3
"""
This module provides a function to query the Reddit API and return the number
of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a
    given subreddit.
    If an invalid subreddit is given, the function returns 0.
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'MyAPIProject/0.0.1'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException:
        return 0


# Example usage
if __name__ == "__main__":
    subreddit = input("Enter the name of the subreddit: ")
    subscribers = number_of_subscribers(subreddit)
    print(f"Number of subscribers in r/{subreddit}: {subscribers}")
