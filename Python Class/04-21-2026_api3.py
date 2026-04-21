import requests

r = requests.get('http://api.open-notify.org/iss-now.json')
# This gives us the number value only
longi = r.json()['iss_position']['longitude']
lati = r.json()['iss_position']['latitude']
# print(r)
# print(r.json())
print(f"The longitude is {longi}")
print(f"The latitude is {lati}")
print(r.json()['iss_position'])
