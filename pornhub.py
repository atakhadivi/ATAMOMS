import requests

url = 'http://www.pornhub.com/rss'
response = requests.get(url)

if response.status_code == 200:
    rss_feed = response.text
    print(rss_feed)
else:
    print(f'Failed to fetch RSS feed. Status code: {response.status_code}')
