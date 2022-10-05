from datetime import date, datetime
import json,requests,sys
from urllib import response
APPID='fc56ca2f05fa1baa407711c533c0ea8d'

if len(sys.argv)<2:
    print('Usage: weather_map.py city_name 2-letter_country_code')
    sys.exit()
location=','.join(sys.argv[1:])
print(location)

#url ='http://api.openweathermap.org/data/2.5/weather?q=%s&dt=%d&appid=%s'% (location,dt,APPID)
url=f'https://api.openweathermap.org/data/2.5/forecast?q={location}&cnt=5&appid={APPID}'
print(url)
#vrl='http://api.openweathermap.org/data/2.5/weather?q=Tezpur,IN&cnt=3&appid=fc56ca2f05fa1baa407711c533c0ea8d'

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




















# total arguments
# n = len(sys.argv)
# print("Total arguments passed:", n)
 
# # Arguments passed
# print("\nName of Python script:", sys.argv[0])
 
# # print("\nArguments passed:", end = " ")
# # for i in range(1, n):
# #     print(sys.argv[i])
# location=''.join(sys.argv[1:])
# print(location+'qwq')
     