import requests
url = input('Input the URL: ')
r = requests.get(url)
if r.status_code == 200:
    file = open('source.html', 'wb')
    file.write(r.content)
    file.close()
    print('Content saved.')
else:
    print(f'The URL returned {r.status_code}')
