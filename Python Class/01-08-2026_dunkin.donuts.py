import requests
from bs4 import BeautifulSoup


# Grab info from an url
url = "https://www.dunkindonuts.com/en/menu"

# function
def get_website(url):
# Extract title from a page (url)
    response = requests.get(url)
    donuts = BeautifulSoup(response.content , "html.parser")
# print(donuts.title)
    return donuts.title

# Extract article paragraph (Summary)
content = get_website(url)
print(content)
# Extract article heading