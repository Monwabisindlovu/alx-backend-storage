#!/usr/bin/env python3
"""
Web module for implementing an expiring web cache and tracker
"""
import requests
import redis
import time


def get_page(url: str) -> str:
    """
    Retrieve the HTML content of a URL and cache the result
    with an expiration time of 10 seconds.
    Also track how many times the URL was accessed.
    Args:
        url: The URL to retrieve the HTML content from.
    Returns:
        The HTML content of the URL.
    """
    # Connect to Redis
    redis_client = redis.Redis()

    # Increment the count of accesses for this URL
    url_count_key = f"count:{url}"
    redis_client.incr(url_count_key)

    # Check if the HTML content is cached
    cached_content = redis_client.get(url)
    if cached_content:
        return cached_content.decode()

    # If not cached, fetch the HTML content from the URL
    response = requests.get(url)
    html_content = response.text

    """ Cache the HTML content with an expiration
    time of 10 seconds"""
    redis_client.setex(url, 10, html_content)

    return html_content


if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk/delay/1000/url/http://www.google.com"
    start_time = time.time()
    print(get_page(url))
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")
