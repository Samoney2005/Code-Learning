import requests
from bs4 import BeautifulSoup


url = "https://www.fox4news.com/"

response = requests.get(url)

# to get the content
soup = BeautifulSoup(response.content, "html.parser")
# print(response.text[:1000])
print(soup.head.text)