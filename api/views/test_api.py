import requests

print('REQUEST #1')
r = requests.get("http://127.0.0.1:8000/api/products/?name=bag")
print(r.json())

print('REQUEST #2')
r2 = requests.get("http://127.0.0.1:8000/api/products/?name=a&minprice=100&maxprice=102")
print(r2.json())
