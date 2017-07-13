from bs4 import BeautifulSoup
import requests
import time
import re

# Bloomberg Internet proxy servers
proxies = {'http' : 'proxy.bloomberg.com:81',
           'https': 'proxy.bloomberg.com:81'}

# URL you want to scrape
page = requests.get("https://www.pexels.com/search/nature%20wallpaper/",proxies=proxies)

# Declare soup instance
soup = BeautifulSoup(page.content, 'html.parser')

# Use regex to search for pattern in HTML

start = 0

while start < 10:
    results = soup.find_all(title=re.compile("Nature"))
    start += 1

    print(results)
