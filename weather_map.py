from datetime import date, datetime
import json,requests,sys
from urllib import response
APPID='add your own id'

if len(sys.argv)<2:
    print('Usage: weather_map.py city_name 2-letter_country_code')
    sys.exit()
location=','.join(sys.argv[1:])
print(location)


url=f'https://api.openweathermap.org/data/2.5/forecast?q={location}&cnt=5&appid={APPID}'
print(url)

response=requests.get(url)
response.raise_for_status
weatherdata =json.loads(response.text)

if weatherdata['cod']!='200':
    print(weatherdata['message'])
else:
    w= weatherdata['list']
    i=1
    for data in w:
        print(f'Day {i}: {location}:')
        print(data['weather'][0]['main'],'-',data['weather'][0]['description'])
        i+=1
        print()





















     
