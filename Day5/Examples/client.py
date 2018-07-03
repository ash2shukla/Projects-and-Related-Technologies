from requests import post
from json import loads


username = 'troll'
password = '!23ashish'

url ='http://localhost:8000/'

data = loads(post(url, data= {'user': username, 'pass': password}).text)

url_verify = 'http://localhost:8000/verify/'

print(post(url_verify, data= data).text)
