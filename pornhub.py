import feedparser
import requests

# Fetch the RSS feed
url = 'http://www.pornhub.com/rss'
response = requests.get(url)

if response.status_code == 200:
    rss_feed = response.text

    # Parse the RSS feed
    feed = feedparser.parse(rss_feed)
    # print(feed)
    # Extract the feed title and list of entries
    entries = feed.entries
    # print(entries[0].title)
    # Print the feed title and first entry title
    # print('Feed title:', title)
    print('First entry title:', entries[0].title)
else:
    print(f'Failed to fetch RSS feed. Status code: {response.status_code}')
