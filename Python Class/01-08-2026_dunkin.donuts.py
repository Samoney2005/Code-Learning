import requests
from bs4 import BeautifulSoup


# Grab info from an url
url = "https://www.dunkindonuts.com/en/menu"

# function
def get_website(url):
    # Extract title from a page (url)
    response = requests.get(url)
    donuts = BeautifulSoup(response.content, "html.parser")
    return donuts

# Extract article paragraph (Summary) – here: page title
page = get_website(url)
title = page.title.get_text(strip=True) if page.title else "No title found"
print("Page title:", title)

# Extract article heading
# Example: grab all h1 and h2 texts as headings
headings = []

for tag in page.find_all(["h1", "h2"]):
    text = tag.get_text(strip=True)
    if text:
        headings.append(text)

print("Headings:")
for h in headings:
    print("-", h)
