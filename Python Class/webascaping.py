import requests
from bs4 import BeautifulSoup


url = "https://www.fox4news.com/"

response = requests.get(url)
# print(response.text[:1000])
print(response.head)