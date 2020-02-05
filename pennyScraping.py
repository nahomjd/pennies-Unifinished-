import requests
url = 'http://209.221.138.252/AreaList.aspx'
headers = {'User-Sgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}

response =  requests.get(url, headers=headers)
lines = response.text.split("\n")
loc = 0 
location = []
Llist = []
for x in lines:
    #print(x)
    if loc == 1:
        country = x.split("\t")[7].split("<")[0]
        #print(country)
        location.append(country)
        Llist.append(location)
        #print(location)
        location = []
        loc = 0
    if 's.aspx' in x:
        link = x.split("='")[1].split("'>")[0]
        location.append(link)
        area = link.split("=")[1]
        location.append(area)
        #print(link)
        #print(area)
        loc = 1
        
print(Llist)