import requests
'''
lat = 32.779167
lng = -96.808891
r = requests.get('https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400')
'''

payload = {'lat': '32.779167', 'lng': '-96.808891'}
r = requests.get('https://api.sunrise-sunset.org/json', params=payload)

print(r)
#print(r.json())
# This prints the sunrise time
sun = r.json()['results']['sunrise']
print(f"The sunrise time is {sun}")
# This prints the time
print(sun.split()[0])
print(sun.split()[0].split(":")[1])


