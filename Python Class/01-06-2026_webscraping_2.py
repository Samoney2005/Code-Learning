import requests

url = "https://www.makefaire.com"
r = requests.get(url)
print(r.status_code)
# if the status_code = 200 r.text will print
if r.status_code == 200:
    print(r.text)
else:
    print(f"Failed Attempt{r.status_code}")
