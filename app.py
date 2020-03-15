import requests

requests = requests.get('https://api.kanye.rest/?format=text')
qoute = requests.content

print(qoute)