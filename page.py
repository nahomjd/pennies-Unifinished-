import requests
#import pandas as pd 
url = 'http://209.221.138.252/Locations.aspx?area=41'
headers = {'User-Sgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}

response =  requests.get(url, headers=headers)
lines = response.text.split("\n")
loc = 0 
name = []
addresses = []
cities = []
Designs = []
updated = []

#looking for <br /><
for x in lines:
    #print(x) '<br /><
    if '<br /><' in x:
        if '<s>' in x:
            location = x.split('</s>')[0].split('<s>')[1]
        else:
            location = x.split('<br /')[0].split('>')[1]
        name.append(location)
        address = x.split('</span')[0].split("e'>")[1]
        addresses.append(address)
        city = x.split('</td><td')[1]
        city = city[1:]
        cities.append(city)
        s = x.split('</td><td')[2].split('>')[1]
        Designs.append(s)
        date = x.split('"Center">')[3].split('<')[0]
        print(date)
        update.append(date)