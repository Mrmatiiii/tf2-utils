import requests
import json

data = []
file = 'bots.json'

r = requests.get('https://api.tf2automatic.com/v1/bots').json()

if r['success'] == True:
    for i in r['result']:
        data.append(int(i['steamid']))
    print('All {} tf2automatic bots were written to {}'.format(len(r['result']), file))
else:
    print('Error. Wrong response from the API')

with open(file, 'w') as outfile:
    json.dump(data, outfile, indent=4)
