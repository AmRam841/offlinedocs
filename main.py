from src.offlinedocs.scraper import fetcher
from bs4 import BeautifulSoup


fetched = fetcher.Fetcher("https://www.geeksforgeeks.org/python/beautifulsoup4-module-python/")
print(fetched)

soup = BeautifulSoup(fetched.response.text , 'html.parser')
print(soup.prettify())


