#!/usr/bin/python3
"""
This module provides a recursive function to query the Reddit API,
parse the titles of all hot articles, and print a sorted count of
given keywords.
"""

import requests
from collections import Counter


def count_words(subreddit, word_list, after=None):
    """
    Queries the Reddit API recursively, parses the titles of all hot articles,
    and prints a sorted count of given keywords.
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
            titles = [post['data']['title'] for post in posts]
            parse_titles(titles, word_list)
            after = data['data']['after']
            if after is not None:
                count_words(subreddit, word_list, after)
        else:
            return
    except requests.RequestException:
        return


def parse_titles(titles, word_list):
    """
    Parses the titles of Reddit posts and prints a sorted count of
    given keywords.
    """
    word_count = Counter()
    for title in titles:
        words = title.lower().split()
        for word in words:
            word = word.rstrip('.!_')  # Remove trailing special characters
            if word in word_list:
                word_count[word] += 1

    sorted_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_count:
        print(f"{word}: {count}")


# Example usage
if __name__ == "__main__":
    subreddit = input("Enter the name of the subreddit: ")
    word_list = input(
        "Enter the list of keywords separated by spaces: "
    ).split()
    count_words(subreddit, word_list)
