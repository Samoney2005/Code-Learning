import requests

r = requests.get('http://api.open-notify.org/iss-now.json')
longi = r.json()['iss_position']['longitude']
lati = r.json()['iss_position']['latitude']
print(r)
print(r.json())
print(lati)
print(longi)
#print(r.json()['iss_position']['longitude'])
