import requests
url = input('Input the URL: ')
r = requests.get(url)
data = r.json()
if r.status_code == 200 and 'content' in data:
    print(data['content'])
else:
    print('Invalid quote resource!')