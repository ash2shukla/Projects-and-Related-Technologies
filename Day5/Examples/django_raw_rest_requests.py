from requests import put, get, post, delete

url = "http://localhost:8000/demo/"
print(put(url, data={'attr1': '123', 'attr2': '456'}).text)
print(get(url, params={'attr1': '123'}).text)
print(post(url, data={'attr1_from': '123', 'attr1_to': 'abc'}).text)
print(get(url, params={'attr1': 'abc'}).text)
print(delete(url, data={'attr1': 'abc'}).text)
