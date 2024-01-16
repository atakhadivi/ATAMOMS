import feedparser
import requests

# Fetch the RSS feed
url = 'http://www.pornhub.com/rss'
response = requests.get(url)

if response.status_code == 200:
    rss_feed = response.text

    # Parse the RSS feed
    feed = feedparser.parse(rss_feed)

    # Filter entries containing the keyword 'mom'
    mom_entries = [
        entry for entry in feed.entries if 'mom' in entry.title.lower()]

    # Print the number of filtered entries
    print(f"Number of entries containing 'mom': {len(mom_entries)}")

    # Print the titles of the filtered entries
    for entry in mom_entries:
        print(entry.title)
else:
    print(f'Failed to fetch RSS feed. Status code: {response.status_code}')
