import requests

#url = "https://en.wikipedia.org/wiki/Web_scraping"
url = "https://www.makefaire.com"
r = requests.get(url)
print(r.text)